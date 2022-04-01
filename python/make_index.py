'''
Loop over stuff in order to make website, print HTML to file.
'''
import numpy as np
import os 
import glob 

# HOMEPAGE 

top = f'''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="s.css">
    <title>IPM Galaxy Movies</title>
  </head>
  <body>

<div class="container">
  <h1> Quenching in Cosmic Sheets</h1>
  <p></p>
  <p>In the gallery below, you can find snapshot movies of the galaxies discussed in Pasha et al. (2022). The movies run from roughly redshift 7 to redshift 2. For most of these systems, the initial cold medium heats during an accretion shock event propagated by the collision of two cosmic sheets. In movies with both a black and white circle, the black circle traces 2 times the half mass radius of the subfind object being tracked, while the white circle in all cases traces the virial radius of the FoF group. The two panels in each movie show viewing angles face on (top) and edge on (bottom) with respect to the cosmic sheet.</p>
'''

# Calculate N rows

n_rows = int(np.ceil(len(glob.glob('../pages/Stamps/*/',recursive=True))/3.0))

galaxies = [i.split('/')[3] for i in glob.glob('../pages/Stamps/*/',recursive=True)]
gal_nums = sorted([int(i.split('g')[1]) for i in galaxies])
galaxies = ['g'+str(i) for i in gal_nums]
counter = 0

write_string = ''''''

for i in range(n_rows):
    row = f'''
    <div class="row mt-5">
    '''
    for j in range(3):
        try:
            print(galaxies[counter])
        except:
            continue
        add = f'''
        <div class="col">
            <div class="card h-100" style="width: 18rem;">
                <img class="card-img-top" src="pages/Stamps/{galaxies[counter]}/png/cover.png" alt="Snapshot {galaxies[counter]} of this galaxy">
                <div class="card-body">
                    <h5 class="card-title">Galaxy {galaxies[counter].split('g')[1]}</h5>
                    <a href="pages/{galaxies[counter]}.html" class="btn btn-primary">See Movie</a>
                </div>
            </div>
        </div>
        '''
        counter += 1
        row += add 
    row+= "</div>"
    write_string+=row

write_string = top+write_string+'</div>' + '''
   <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
  </body>

</html>
'''
with open('test.html','w') as f:
    f.write(write_string)
