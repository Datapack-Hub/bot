import disnake
from disnake.ext import commands
import variables
import re

def fancify(command):
    cmds_raw: list[str] = []
    
    combine = False;
    for line in command:
        if combine:
            cmds_raw[-1] += line + '\n'
        else:
            cmds_raw.append(line + '\n')
        combine = line.endswith('\\')
    
    cmds: list[dict[str,str]] = []
    
    for line in cmds_raw:
        if line.startswith('#'):
            cmds.append({
                "text": line,
                "type": "comment",
            })
        elif line.startswith('$'):
            word = re.match(r'^\$\w* ?', line)
            is_say = re.match(r'^\$say ?', line) or re.match(r'^\$me ?', line)
            cmds.extend([{
                "text": word[0],
                "type": "macro",
            }, {
                "text": line.removeprefix(word[0]),
                "type": "message" if is_say else "",
            }])
        elif line.startswith('say') or line.startswith('$say') or line.startswith('me') or line.startswith('$me'):
            word = re.match(r'^\$?\w* ?', line)
            is_say = re.match(r'^say ?', line) or re.match(r'^me ?', line)
            cmds.extend([{
                "text": word[0],
                "type": "command",
            }, {
                "text": line.removeprefix(word[0]),
                "type": "message" if is_say else "",
            }])
        elif line:
            word = re.match(r'^\w* ?', line)
            cmds.extend([{
                "text": word[0],
                "type": "command",
            }, {
                "text": line.removeprefix(word[0]),
                "type": "",
            }])
        else:
            cmds.append({
                "text": line,
                "type": "",
            })
    
    
    
    def match(pattern: str, kind: str, prev_kind: str, line: str):
        out = []
        last = 0
        for m in re.finditer(pattern, line):
            out.extend([{
                "text": line[last:m.span()[0]],
                "type": prev_kind,
            }, {
                "text": m[0],
                "type": kind,
            }])
            last = m.span()[1]
        out.append({
            "text": line[last:],
            "type": prev_kind,
        })
        return out
    
    def match_compound(start:str, end:str, kind:str, prev_kind:str, line:str) -> list[dict[str,str]]:
        out = [{"text":"","type":prev_kind}]
        depth = 0
        is_bs = False
        is_string = False
        for ch in line:
            if is_bs:
                is_bs = False
            elif ch == '"':
                is_string = not is_string
            elif ch == start and not is_string:
                if depth == 0: out.append({"text":"","type":kind})
                depth += 1
            elif ch == end and not is_string:
                if depth == 1: out.append({"text":"","type":prev_kind})
                if depth > 0: depth -= 1
            elif ch == '\\':
                is_bs = True
            out[-1]["text"] += ch
        return out

    def replace_compound(before:list[str], start:str, end:str, kind:str, repl:list[str], arr:list[dict[str,str]]):
        out = []
        should_match = len(before) == 0
        for cmd in arr:
            if cmd['type'] in repl and should_match:
                out.extend(match_compound(start, end, kind, cmd['type'], cmd['text']))
                should_match = len(before) == 0
            elif cmd['type'] in before:
                should_match = True
                out.append(cmd)
            else:
                out.append(cmd)
        return out
    
    def replace(pattern: str, kind: str, array: list[dict[str,str]], repl: list[str]) -> list[dict[str,str]]:
        out = []
        for cmd in array:
            if cmd['type'] in repl:
                out.extend(
                    match(
                        pattern,
                        kind,
                        cmd['type'],
                        cmd['text'],
                    )
                )
            else:
                out.append(cmd)
        return out
    
    def replace_all(arr:list[dict[str,str]], *args) -> list[dict[str,str]]:
        for arg in args:
            if len(arg) == 5:
                arr = replace_compound(arg[0], arg[1], arg[2], arg[3], arg[4], arr)
            elif len(arg) == 3:
                arr = replace(arg[0], arg[1], arr, arg[2])
        return arr
    
    final = replace_all(cmds,
        (r'(?<=run say )(.*?\\\n|.*)+',                        "message",   [""]),
        (r'(?<=run me )(.*?\\\n|.*)+',                         "message",   [""]),
        (r'(?<=run \\\n)\s*(say|me) (.*?\\\n|.*)+',            "say",       [""]),
        (r'^\s*say |^\s*me ',                                  "command",   ["say"]),
        (r'(.*\n?)+',                                          "message",   ["say"]),
        (r'(^| )@[aepsr]',                                     "selector@", ["","message"]),
        (["selector@"], '[', ']',                              "selector",  ["","message"]),
        ([],            '{', '}',                              "snbt",      ["","selector"]),
        (r'(?<!\\)(\\{2})*"(.*?(\\\n)?)+(?<!\\)(\\{2})*"',     "string",    ["","snbt","selector"]),
        (r'([\w\d_\-]*:[\w\d_\-/]+)|([\w\d_\-]+:[\w\d_\-/]*)', "resource",  ["","selector"]),
        (r'(?<=run )\w+|(?<=run \\\n)\s*\w+',                  "command",   [""]),
        (r'\b-?\d+(\.\d+)?\b',                                 "number",    ["","snbt","selector"]),
        (r'\\\n',                                              "\\",        ["","snbt","string","selector","message"]),
        (r'\$\([a-z_\-0-9]+\)',                                "var",       ["","string","number","selector","message"]),
        (r'[\[\]\{\}]',                                        "bracket",   ["","snbt","selector"]),
        (r'<[a-zA-Z_0-9\-\. ]*>',                              "highlight", ["","snbt","selector","string","var","message"]),
    )

    # print(final) # debug output
    
    output_value = ""
    for d in final:
        if d['type'] in ["comment", "\\"]:
            output_value += '\033[0;30m' + d['text'] # black
        elif d['type'] in ["macro", "var"]:
            output_value += '\033[0;31m' + d['text'] # red
        elif d['type'] in ["string", "message"]:
            output_value += '\033[0;33m' + d['text'] # yellow
        elif d['type'] in ["resource", "bracket"]:
            output_value += '\033[0;34m' + d['text'] # blue
        elif d['type'] in ["command"]:
            output_value += '\033[0;35m' + d['text'] # magenta
        elif d['type'] in ["number", "selector@"]:
            output_value += '\033[0;36m' + d['text'] # cyan
        elif d['type'] in ["highlight"]:
            output_value += '\033[0;31;47m' + d['text'] # red with white bg
        else:
            output_value += '\033[0;39m' + d['text'] # reset

    return output_value
         
class FancifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Fancify ✨")
    async def fancify(self, inter: disnake.MessageCommandInteraction,message):
        p = re.compile(r"(?<!\\)(\\{2})*```(.*?(?<!\\))(\\{2})*```", flags=re.DOTALL)
        matches = re.findall(p,message.content)
        for match in matches:
            lines = match[1].split('\n')
            if re.match(r"^[a-z]+$", lines[0]): lines = lines[1:]
            while lines and lines[0] == '': lines.pop(0)
            while lines and lines[-1] == '': lines.pop()
            output = fancify(lines)
        if (not message.embeds) and (not message.stickers) and (not message.attachments):
            if matches:
                embed = disnake.Embed(
                    description="```ansi\n" + output + "\n```",
                    color=disnake.Colour.purple()
                )
                
            else:
                output = fancify((message.content).split('\n'))
                embed = disnake.Embed(
                    description="```ansi\n" + output + "\n```",
                    color=disnake.Colour.purple()
                )  
                
            embed.set_footer(text=f"Requested by {inter.user.name} ✨", icon_url=inter.user.avatar)
            await inter.target.reply(embed=embed,allowed_mentions=None)
            await inter.response.send_message("Fancification successful :sparkles:", ephemeral=True)

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Fancify` Message Command**"),
                description=(
                    str(inter.user.name)
                    + "Fancified a message! "
                    + str(message.jump_url)
                    + " (Server: **"
                    + inter.guild.name
                    + "**)"
                )
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
        
        else:
            await inter.response.send_message("You can't fancify this message!", ephemeral=True)
                
            