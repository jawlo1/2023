<?php
    $servername="localhost";
    $username="root";
    $password="";
    $dbname="baza";

    $conn=mysqli_connect($servername,
                        $username,
                        $password,
                        $dbname);
    if( !$conn ){
        die("Nieudane połączeni". mysqli_connect_error());
    }
    $data=$_POST["data"];
    $liczba=$_POST["osob"];
    $telefon=$_POST["telefon"];

    $sql="insert into rezerwacje(data_rez,
                            liczba_osob,
                            telefon) values($data,
                            $liczba, $telefon)";
    echo "sql=".$sql;
    if( mysqli_query( $conn, $sql ) ){
        echo "Dodano rezerwacje do bazy";
    }else{
        echo "błąd: ".mysqli_error($conn);
    }
