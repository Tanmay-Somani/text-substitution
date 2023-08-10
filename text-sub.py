import keyboard

text_substitutions = {
  "hru": "How are you",
  "hlw": "Hello",
  "PROfile":"my linkedin is https://www.linkedin.com/in/tcode/"
    # Add more substitutions as required by you
}

def expand_text(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == "space":
        text = keyboard.get_typed_strings(e)
        for trigger, replacement in text_substitutions.items():
            if trigger in text:
                expanded_text = text.replace(trigger, replacement)
                keyboard.write(expanded_text) #here is the code via which you expand your text by replacing by performing your certain tasks

# Hooking the keyboard event
keyboard.hook(expand_text)

# Keeping the script runnin
keyboard.wait("esc")
