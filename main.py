def do_magic():
    from html2image import Html2Image

    hti = Html2Image()
    with open('./example_input.html') as f:
        hti.screenshot(f.read(), save_as='example_output.png')

if __name__ == "__main__":
    do_magic()