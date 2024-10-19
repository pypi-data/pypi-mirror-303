from fasthexgen.commands.template import HexTemplate, BaseTemplate

def hexagonal_template_genrator(argv) -> BaseTemplate:
    if argv[1] == "createproject":
        try:
            project_name = argv[2]
            return HexTemplate(project_name)
        except:
            return HexTemplate()
    return None

"__all__" == ['hexagonal_template_genrator']