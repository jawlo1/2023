<?php
    // utworzenie nowego pliku i zapis
    // tekstu do niego

    $myFile = fopen("newfile.txt","w")
                or die("Unable to open file");
    $tekst = "John już tu nie mieszka";
    fwrite( $myFile, $tekst );
    fclose( $myFile );