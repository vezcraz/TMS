var i = 0;
var speed = 100; 


var devs=[

{
	'Name':'Keshav Nagpal',
	'Img':'keshav.jpg		',
	'Desc':'I provide web design hosting services, SEO, front-end and back-end development I specialize in standards-based XHTML,CSS and Javascript development. I have also worked with various organizations, building their Database Management System and developing software for their day-to-day work. ',
	'LinkedIn':'https://www.linkedin.com/in/ritiktaneja',
	'GitHub':'https://github.com/ritiktaneja',
	'Web':'https://www.ritiktaneja.in',
	'Mail':'mailto:ritiktaneja10@gmail.com'

},
{
	'Name':'Ritik Taneja',
	'Img':'ritik.jpg',
	'Desc':'I provide web design hosting services, SEO, front-end and back-end development I specialize in standards-based XHTML,CSS and Javascript development. I have also worked with various organizations, building their Database Management System and developing software for their day-to-day work. ',
	'LinkedIn':'https://www.linkedin.com/in/ritiktaneja',
	'GitHub':'https://github.com/ritiktaneja',
	'Web':'http://www.ritiktaneja.in'

}]


  function display(num)
{

 i = 0;
speed = 100; 

	document.getElementById('content-1-1').innerHTML="";
		document.getElementById('content-1-2').innerHTML="";
		document.getElementById('content-2').innerHTML="";
	addLinks(num);
	typeWriter(devs[num].Desc);
	showImage(devs[num].Img);
}


	function addLinks(val)
	{	
		//var links=document.createElement('div');

		var github=`<a class='p-2' href='`+devs[val].GitHub+`' ><img height="32" width="32" src="{% static 'grievance/images/github.svg' %}" /></a>`;
		var linkedin=`<a class='p-2' href='`+devs[val].LinkedIn+`' ><img height="32" width="32" src="{% static 'grievance/images/linkedin.svg' %}" /></a>`;
		var web=`<a class='p-2' href='`+devs[val].Web+`' ><img height="32" width="32" src="{% static 'grievance/images/internetexplorer.svg' %}" /></a>`;
		var mail=`<a class='p-2' href='`+devs[val].Mail+`' ><img height="32" width="32" src="/ grievance/images/gmail.svg" /></a>`;
		var links=`<div class="text-center" style="fill:white; color:white;">`+github+linkedin+web+mail+`</div>`
		document.getElementById('content-1-1').insertAdjacentHTML('afterbegin',links);
	}

	

	function showImage(src)
  {
  	console.log(src);
  	
  	document.getElementById('content-2').innerHTML="<img data-aos='fade-in' src="+src+" id='devImg' class='container-fluid img'></img> ";

  	blinkImg(1,1000,1);

  }


function blinkImg(x,speed1,count)
{

f=document.getElementById("devImg");


speed1=speed1-500;




if(x)
f.style.display="block";

else
 f.style.display="none";


count++;
if(count<55)
 setTimeout("blinkImg("+!x+","+speed1+","+count+")",speed1);
	else
	{f.style.display="block";
					
	}

  
}



function typeWriter(txt) {



	//console.log("hereee"+txt);
  if (i < txt.length) {
   document.getElementById("content-1-2").innerHTML += txt.charAt(i);
    i++;
    
  //   if(i==txt.length)
  //   { 
  //   	var now=(new Date()).getTime();
  //   	while ( new Date().getTime() < now + 5000 )
		// {	

		// }
  //   	document.getElementById('content-1').innerHTML="";
  //   	i=0;
  //   }


    setTimeout("typeWriter('"+txt+"')", speed);


  }

  


}
