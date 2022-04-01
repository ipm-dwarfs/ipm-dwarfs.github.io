
def make_page(gal):
    top = '''
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel="stylesheet" href="../s.css">
        <title>IPM Galaxy Movies</title>
    </head>
    <body>
        <div align='center'>
        <h1>IPM Galaxy Movies</h1>
        <p><a href="../index.html">Home</a></p>
    <div align="center">
    <div class="card" style="width: 30rem;">
    <div class="card-body">
        <div id="carouselExampleControls" class="carousel slide carousel-fade" data-ride="carousel" data-interval="75">
        <div class="carousel-inner">
    '''

    for i in range(78,123):
        if i == 78:
            item = f'''
            <div class="carousel-item active">
            <img class="d-block w-100" src="Stamps/g{gal}/png/Snap_{i}.png" alt="First slide">
            </div>
            '''
        else:
            item = f'''
            <div class="carousel-item">
            <img class="d-block w-100" src="Stamps/g{gal}/png/Snap_{i}.png" alt="First slide">
            </div>
            '''
        top += item 
    bottom = f'''
                </div>
                <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>
                <p></p>
                <h4 class="card-title">Galaxy {gal}</h4>
                <p>Hover over the animation to pause on that frame and use the arrows to navigate manually. Move mouse to resume playing.</p>
            </div>
            </div>
            <p></p>
            </div>
                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                
            </body>

            </html>
                '''
    final = top + bottom 

    with open(f'g{gal}.html','w') as f:
        f.write(final)