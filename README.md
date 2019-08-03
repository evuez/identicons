# Github-like identicon generator.

Example:

    i = Identicon('johndoe')
    i.generate()
    # Or, generate the base64-encoded image:
    i.base64('PNG')

![identicon](http://dev.evuez.net/dev/tracker/identicon.png)

Do you need to generate SVG instead? https://github.com/evuez/svg-identicon

## Requirements

If there's an error while installing Pillow (with `pip install -r requirements.txt`), you might be missing `python3-devel` or similar depending on your platform.
