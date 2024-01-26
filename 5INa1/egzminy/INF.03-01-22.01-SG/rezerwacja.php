<?php
    $server="localhost";
    $user="root";
    $password="";
    $database="baza";
    
    $con=mysqli_connect($server,$user,$password,$database);
    if( !$con ){
        die("Nie udało się połączyć: ". mysqli_error() );
    }
    $data=$_POST['data'];
    $ile=$_POST['osob'];
    $telefon=$_POST['telefon'];
    $sql="insert into rezerwacje( data_rez, liczba_osob, telefon) 
                           values( $data, $ile, $telefon)";
    echo $sql;

    if( mysqli_query( $con, $sql )){
        echo "Dodano rezerwacje do bazy";
    }else{
        echo "błąd dodania rekordu".mysqli_error($con);
    }
    mysqli_close( $con );
?>