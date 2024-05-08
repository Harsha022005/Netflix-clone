# Netflix-clone
<--A Netflix clone built with HTML and Tailwin css framework.>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netflix-clone</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<style>
  
</style>
<body >
    <div class="head relative border-b-8 border-slate-800" > 
      <-- Add background image-->
                 <img class="object-cover w-full h-full " src="" alt="Background Image">
                <div class="absolute inset-0 bg-black opacity-60"></div>
                <div class="Logo"><p style="color: #c51821;" class="font-bold text-5xl absolute inset-0 w-40 ml-40 mt-10 ">NETFLIX</p></div>
                <div class="absolute  top-10 lg:ml-[1200px] " ><button  class="border-2 px-6 py-1 text-white">English</button></div>
                <div class="absolute  top-10  lg:ml-[1300px] " ><button  class=" bg-red-600 border-red-700 ml-10  border-2 px-6 py-1 text-white">Sign-in</button></div>
   
                <div class="absolute top-80 lg:ml-[350px]">
                    <div class=" text-white font-bold text-5xl truncate "><pre class="font-sans text-clip overflow-hidden ">Unlimited movies, TV shows and more</pre></div>
                    <div class=" ml-44 mt-5 text-slate-300 font-bold text-3xl "><p>Watch anywhere. Cancel anytime.</p></div>
                    <div class=" -ml-10 mt-10 text-slate-300  font-bold text-2xl "><p>Ready to watch? Enter your email or mobile number to create or restart your membership.</p></div>
                     
                    <div class="bot relative ">
                        <div class="email "><input class=" bg-black opacity-50 mt-10 ml-20 px-28 py-4 border-2 border-white text-white hover: bg-black opacity-40 " type="text"placeholder="Email or mobile number"></div>
                      <div class="absolute  top-10 lg:ml-[500px]" ><button style="background-color: #ff000d;"  class=" border-red-700  border-2 px-20 py-3 text-white font-bold">Get-Started</button></div>
   
                    </div>
                </div>
               
                
    </div>       
    <div class="sec-1 max-w-600 max-h-600 bg-black flex border-b-8 border-slate-800">
         <div class="cont text-white mt-40 mb-40 ml-40 space-y-3 font-bold ">
            <p class="text-5xl" >Enjoy on your TV</p>
            <p class="text-2xl">Watch on smart TVs, PlayStation, Xbox,Chromecast,</p>
            <p class="text-2xl"> Apple TV, Blu-ray players and more.</p>
         </div>
         <div class="img">
            <img  class="mt-20 ml-40 " src="https://occ-0-2794-2219.1.nflxso.net/dnm/api/v6/rkETp35xJVj-6WaffQsS77awykM/AAAABQ4J7tcinnCNOAlVYzjC_C0_xYHRPPk5yO8R9gGkT2kzYLslv9bvSuTfZcJT3FdKozy3kW6tMT-fhwLO8DeeEhsVwAbB7BIfniEaM96KOnV2FTjkP7zVLHVthBu-nc1Y4vxVuisQRxl9DwI7HvTcoVkDEFRcRlFQltwKFjQayLFO1GXJMrttG9z4-Lse_cP9q4iRvRB8ZibuWUbqtmknWTEiANjDRU09QZRu.jpg?r=c68" alt="">
         </div>
        
    </div>

    <div class="sec-2 max-w-600 max-h-600 bg-black flex border-b-8 border-slate-800">
      
        <div class="img">
           <img  class="mt-20 ml-40 " src="https://occ-0-2794-2219.1.nflxso.net/dnm/api/v6/19OhWN2dO19C9txTON9tvTFtefw/AAAABVr8nYuAg0xDpXDv0VI9HUoH7r2aGp4TKRCsKNQrMwxzTtr-NlwOHeS8bCI2oeZddmu3nMYr3j9MjYhHyjBASb1FaOGYZNYvPBCL.png?r=54d" alt="">
        </div>
        <div class="cont text-white mt-40 mb-40 ml-20 space-y-3 font-bold ">
            <p class="text-5xl" >Create profiles for kids</p>
            <p class="text-2xl">Send children on adventures with their favourite</p>
            <p class="text-2xl"> Send children on adventures with their favourite</p>
            <p class="text-2xl"> your membership.</p>
        </div>
   </div>  
    
   <div class="sec-3 max-w-600 max-h-800 bg-black pb-20  space-y-3 border-b-8 border-slate-800">
       <p class="   cont text-white mb-20 ml-96 font-bold text-6xl">Frequently Asked Questions</p>
       <p class="q-1 text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">What is Netflix?</p>
      <p class="q-2  text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">How much does Netflix cost?</p>
      <p class="q-3  text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">Where can I watch?</p>
      <p class="q-4  text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">How do I cancel?</p>
       <p class="q-5  text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">What can I watch on Netflix?</p>
      <p class="q-6  text-3xl text-white ml-20 mr-20 bg-gray-900 px-20 py-4 hover:bg-gray-800">Is Netflix good for kids?</p>
     
      <div class="below ">
        <p class="ml-48 mt-20 text-slate-300  font-bold text-2xl" >Ready to watch? Enter your email or mobile number to create or restart your membership.</p>
        <div class="bot relative ">
            <div class="email ">
                <input class=" bg-black opacity-50 mt-10 ml-96 px-28 py-4 border-2 border-white text-white hover: bg-black opacity-40 " type="text"placeholder="Email or mobile number"></div>
                <div class="absolute  top-11 lg:ml-[800px]" ><button style="background-color: #ff000d;"  class=" border-red-700  border-2 px-20 py-3 text-white font-bold">Get-Started</button></div>
        </div>
    </div>
</div>  
    <div class="footer bg-black">
        <footer class="py-3  text-white">
            <ul class="nav justify-content-center border-bottom pb-3 mb-3">
                <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Home</a></li>
                <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Features</a></li>
                <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Pricing</a></li>
                <li class="nav-item"><a href="#" class="nav-link px-2 text-white">FAQs</a></li>
                <li class="nav-item"><a href="#" class="nav-link px-2 text-white">About</a></li>
            </ul>
            
            <p class="text-center  text-white">© 2024 Company, Inc</p>
          </footer>
    </div>
</body>

</html>
