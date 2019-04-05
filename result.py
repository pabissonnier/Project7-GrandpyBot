#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """
<!DOCTYPE html>
<html lang="fr" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="..\bootstrap-4.3.1\dist\css\bootstrap.css" rel="stylesheet">
    <link href="style.css" rel="stylesheet">

    <title>GrandPy Bot</title>

</head>

<body>
    <header>
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-4">
                    <img src="images\logo.png" alt="Logo de GrandPy Bot">
                    <h2>GrandPy Bot</h2>
                </div>
                <div class="col-lg-8">
                    <div class="baseline">
                        <h3> Il sait tout sur tout !</h3>
                    </div>

                </div>
            </div>
        </div>
    </header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Accueil <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">A propos</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
      </div>
    </nav>

    <div class="middlebloc">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-5">
                    <h2>Merci pour ta question !</h2>
                </div>
                <div class="col-lg-7">
                    <p>ZONE POUR DIALOGUE</p>
                </div>

            </div>
        </div>
    </div>
    <footer>
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-4">
                    <div class="name">
                        <h6>Pierre-Antoine Bissonnier</h6>
                    </div>
                </div>
                <div class="col-lg-8">
                    <h6>Où me trouver ?</h6>
                    <p>
                        <a href="https://github.com/pabissonnier" target="_blank"><img src="images/github.png" alt="Vers mon Github"></a>
                        <a href="https://www.linkedin.com/in/pierre-antoine-bissonnier-68885616/" target="_blank"><img src="images/linkedin.png" alt="Vers mon Linkedin"></a>
                        <a href="https://www.malt.fr/profile/pierreantoinebissonnier" target="_blank"><img src="images/malt.png" alt="Vers mon profil Malt"></a>
                    </p>
                </div>
            </div>
        </div>
    </footer>
</body>

</html>

"""

"""question = cgi.FieldStorage()"""

print(html)
