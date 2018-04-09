# Github-like identicon generator.

Example:

    i = Identicon('johndoe')
    i.generate()
    # Or, generate the base64-encoded image:
    i.base64('PNG')

![identicon](http://dev.evuez.net/dev/tracker/identicon.png)

I also made a version that generates SVG: https://github.com/evuez/svg-identicon

## Try it!

[http://dev.evuez.net/dev/identicons/?s=JOHNDOE](http://dev.evuez.net/dev/identicons/?s=JOHNDOE)

## Requirements

If there's an error while installing Pillow (with `pip install -r requirements.txt`), you might be missing `python3-devel` or similar depending on your platform.
