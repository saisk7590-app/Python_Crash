import re
from templates.prompt_templates import TEMPLATES


def detect_template(user):

    user = user.lower()

    if "compare" in user:
        return "comparison"

    if "json" in user:
        return "json_explanation"

    if "steps" in user or "step-by-step" in user or "learn" in user:
        return "step_guide"

    if "summarize" in user or "summary" in user:
        return "summary"

    if "explain" in user:
        return "explanation"

    return None


def fill_template(template_name, user):

    template = TEMPLATES[template_name]

    # comparison
    if template_name == "comparison":

        match = re.search(r'compare\s+(.*?)\s+and\s+(.*)', user, re.IGNORECASE)

        if match:
            item1 = match.group(1)
            item2 = match.group(2)
        else:
            return user

        return template.format(item1=item1, item2=item2)

    # explanation
    if template_name in ["explanation", "json_explanation"]:

        match = re.search(r'explain\s+(.*)', user, re.IGNORECASE)

        if match:
            topic = match.group(1)
        else:
            topic = user

        return template.format(topic=topic)

    # step guide
    if template_name == "step_guide":

        match = re.search(r'learn\s+(.*)', user, re.IGNORECASE)

        if match:
            skill = match.group(1)
        else:
            skill = user

        return template.format(skill=skill)

    # summary
    if template_name == "summary":

        text = user.replace("summarize", "").replace("summary", "")

        return template.format(text=text)

    return user