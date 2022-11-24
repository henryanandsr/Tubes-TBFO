function simpleFor(x)
{
    function fun(){
        console.log("Gak guna");
    }
    for (i = 0; x < 2; x++)
    {
        x = i + 2;
        console.log(i + "iterasi");
    }
    return x;
}