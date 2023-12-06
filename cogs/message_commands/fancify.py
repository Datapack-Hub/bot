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
            word = re.match(r'^$\w* ?', line)
            cmds.extend([{
                "text": word[0],
                "type": "macro",
            }, {
                "text": line.removeprefix(word[0]),
                "type": "",
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
    
    
    
    def match(pattern: str, kind: str, line: str):
        out = []
        last = 0
        for m in re.finditer(pattern, line):
            out.extend([{
                "text": line[last:m.span()[0]],
                "type": "",
            }, {
                "text": m[0],
                "type": kind,
            }])
            last = m.span()[1]
        out.append({
            "text": line[last:],
            "type": "",
        })
        return out
    
    
    def replace(pattern: str, kind: str, array: list[dict[str,str]]) -> list[dict[str,str]]:
        out = []
        for cmd in array:
            if cmd['type'] == "":
                out.extend(
                    match(
                        pattern,
                        kind,
                        cmd['text'],
                    )
                )
            else:
                out.append(cmd)
        return out
    
    def replace_all(arr:list[dict[str,str]], *args) -> list[dict[str,str]]:
        out: list[dict[str,str]] = arr
        for arg in args:
            pattern: str = arg[0]
            kind: str = arg[1]
            replace: list[str] = arg[2] if len(arg) > 2 else [""]
            
            out = replace(pattern, kind, out)
    
    # ignore namespace in json {}
    #
    
    final = replace_all(cmds,
        (r'(?<!\\)(\\{2})*".*?(?<!\\)(\\{2})*"',               "string"  ),
        (r'([\w\d_\-]*:[\w\d_\-/]+)|([\w\d_\-]+:[\w\d_\-/]*)', "resource"),
        (r'(?<=run) \w+|(?<=run \\\n)\n\s+\w+',                "command" ),
        (r'@[aeprs]\[\]',                                      "selector"),
        (r'^-?\d+(\.\d+)?$',                                    "number"  ),
        (r'\\\n',                                              "comment" ),
    )
    
    output_value = ""
    for d in final:
        match d['type']:
            case "comment":
                output_value += '\033[30m' + d['text']
            case "command":
                output_value += '\033[35m' + d['text']
            case "macro":
                output_value += '\033[31m' + d['text']
            case "string":
                output_value += '\033[34m' + d['text']
            case "resource":
                output_value += '\033[33m' + d['text']
            case "number":
                output_value += '\033[36m' + d['text']
            case "selector":
                output_value += '\033[36m' + d['text']
            case _:
                output_value += '\033[34m' + d['text']
    return output_value
         
class FancifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Fancify ✨")
    async def fancify(self, inter: disnake.MessageCommandInteraction,message):
        description_real = ""
        matches = re.findall(r'\`\`\`([\s\S]*?)\`\`\`|\`([\s\S]*?)\`',message.content)
        for match in matches:
            output = fancify(match.split('\n'))
        if (not message.embeds) and (not message.stickers) and (not message.attachments):
            if matches:
                embed = disnake.Embed(
                    description="```hs\n" + output + "\n```",
                    color=disnake.Colour.purple()
                )
                
            else:
                output = fancify((message.content).split('\n'))
                embed = disnake.Embed(
                    description="```ansi\n" + output + "\n```",
                    color=disnake.Colour.purple()
                )  
                
            await inter.target.reply(embed=embed,allowed_mentions=None)
            await inter.response.send_message("Fancification successful :sparkles:", ephemeral=True)

        else:
            await inter.response.send_message("You can't fancify this message!", ephemeral=True)
                
            