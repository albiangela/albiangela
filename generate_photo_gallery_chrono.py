import os

# Define paths to your full-size and thumbnail image directories
thumbs_folder = "images/gallery/thumbs_chrono"
fulls_folder = "images/gallery/fulls_chrono"

# Output HTML file
output_file = "/Users/ang/Dropbox/Work/sharks/code/htmlsite/gallery_chrono_1.html"

# Open a file to write the HTML content
with open(output_file, "w") as html_file:
    # Write the starting structure of the HTML
    html_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aerial</title>
    <link rel="stylesheet" href="assets/css/main.css">
    <script>
        // Disable right-click on all images
        document.addEventListener("contextmenu", function (e) {
            if (e.target.tagName === "IMG") {
                e.preventDefault(); // Prevent the default context menu
            }
        });
    </script>
</head>
<body>
    <header>
        <nav>
            <a href="index.html">Home</a> | <a href="more-photos.html">Back to Gallery</a>
        </nav>
    </header>
    <section id="aerial-photos" class="wrapper style1 align-center">
        <div class="inner">
            <h2>Aerial</h2>
            <div class="gallery style2 medium lightbox">
                <div class="gallery">\n""")


    # Loop through the thumbnails directory to find images
    for thumb in sorted(os.listdir(thumbs_folder)):
        if thumb.endswith((".jpg", ".png", ".jpeg")):  # Only process image files
            # Match the full-size image
            full_image_path = f"{fulls_folder}/{thumb}"
            thumb_image_path = f"{thumbs_folder}/{thumb}"
            
            # Add HTML for each photo
            html_file.write(f"""
                    <article>
                        <a href="{full_image_path}" class="image" data-lightbox="gallery" data-lightbox-options='{{"disableDownload": true}}'>
                            <img src="{thumb_image_path}" alt="Photo">
                        </a>
                    </article>\n""")


    # Close the gallery divs and the HTML structure
    html_file.write("""                </div>
            </div>
        </div>
    </section>
</body>
</html>""")

print(f"HTML gallery generated and saved to {output_file}")