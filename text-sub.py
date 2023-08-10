import keyboard

text_substitutions = {
  "hru": "How are you",
  "hlw": "Hello",
  "PROfile":"my linkedin is https://www.linkedin.com/in/tcode/"
    # Add more substitutions as required by you
}

def expand_text(e):
  global typed_chars
  if e.event_type == keyboard.KEY_DOWN:
    if e.name == "space":
      for trigger, replacement in text_substitutions.items():
        if trigger in typed_chars:
          typed_chars = typed_chars.replace(trigger, replacement)
          keyboard.write(typed_chars)
          typed_chars = ""
        else:
            typed_chars += e.name #here is the code via which you expand your text by replacing by performing your certain tasks

# Hooking the keyboard event
keyboard.hook(expand_text)

# Keeping the script runnin
keyboard.wait("esc")
