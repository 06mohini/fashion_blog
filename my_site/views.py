from django.shortcuts import render
from .models import Feedback



def index(request):
    if request.method == 'POST':

        email = request.POST[ 'email']
        comment = request.POST['message']
        feedback = Feedback(email=email, comment=comment)
        feedback.save()
    else:
        print('not done')

    return render(request,"index.html")    


def about(request):
    return render(request,"about.html") 
def female(request):
    return render(request,"female.html")       
def blog(request):
    return render(request,"blog.html")
def leopard(request):
    return render(request,"pattern/leopard.html")   
def street(request):
    return render(request,"pattern/street.html")     
def tandc(request): 
    return render(request,"tandc.html") 
def indianwear(request):
    return render(request,"femalewears/indianwear.html")  
def westernwear(request):
    return render(request,"femalewears/westernwear.html")        
def saree(request):
    return render(request,"categories/saree.html")
def salwarsuit(request):
    return render(request,"categories/salwarsuit.html")
def lehenga(request):
    return render(request,"categories/lehenga.html") 
def kurtikurta(request):
    return render(request,"categories/kurtikurta.html")
def blouse(request):
    return render(request,"categories/blouse.html") 
def dupattas(request):
    return render(request,"categories/dupattas.html")   
def bottoms(request):
    return render(request,"categories/bottoms.html")   
def ethnicdress(request):
    return render(request,"categories/ethnicdress.html")                 
def ethnicjackets(request):
    return render(request,"categories/ethnicjackets.html")
def casual(request):
    return render(request,"occasions/casual.html") 
def festival(request):
    return render(request,"occasions/festival.html") 
def formal(request):
    return render(request,"occasions/formal.html") 
def evening(request):
    return render(request,"occasions/evening.html") 
def party(request):
    return render(request,"occasions/party.html") 
def work(request):
    return render(request,"occasions/work.html") 
def wedding(request):
    return render(request,"occasions/wedding.html")   
def vacations(request):
    return render(request,"occasions/vacations.html")    
def pants(request):
    return render(request,"types/pants.html")
def churidars(request):
    return render(request,"types/churidars.html")                                     
def skirts(request):
    return render(request,"types/skirts.html") 
def plazzos(request):
    return render(request,"types/plazzos.html")    
def shararas(request):
    return render(request,"types/shararas.html") 
def dhotis(request):
    return render(request,"types/dhotis.html")   
def leggings(request):
    return render(request,"types/leggings.html") 
def checks(request):
    return render(request,"patterns/checks.html")      
def embroidered(request):
    return render(request,"patterns/embroidered.html")  
def floral(request):
    return render(request,"patterns/floral.html")    
def mirror(request):
    return render(request,"patterns/mirror.html")    
def printed(request):
    return render(request,"patterns/printed.html")  
def solid(request):
    return render(request,"patterns/solid.html")       
def stripes(request):
    return render(request,"patterns/stripes.html")  

def dresses(request):
    return render(request,"categories1/dresses.html")  
def tops(request):
    return render(request,"categories1/tops.html")  
def jeans(request):
    return render(request,"categories1/jeans.html")  
def cardigans(request):
    return render(request,"categories1/cardigans.html")  
def gowns(request):
    return render(request,"categories1/gowns.html")  
def jackets(request):
    return render(request,"categories1/jackets.html")  
def jumpsuits(request):
    return render(request,"categories1/jumpsuits.html")  
def Skirts(request):
    return render(request,"categories1/Skirts.html")  
def sweatshirts(request):
    return render(request,"categories1/sweatshirts.html")  
def sets(request):
    return render(request,"categories1/sets.html") 
def Casual(request):
    return render(request,"occasions1/Casual.html") 
def Formal(request):
    return render(request,"occasions1/Formal.html") 
def Work(request):
    return render(request,"occasions1/Work.html") 
def Evening(request):
    return render(request,"occasions1/Evening.html") 
def Vacation(request):
    return render(request,"occasions1/Vacation.html") 
def Ethnic(request):
    return render(request,"occasions1/Ethnic.html") 
def Cocktail(request):
    return render(request,"occasions1/Cocktail.html") 
def Wedding(request):
    return render(request,"occasions1/Wedding.html") 
def Festival(request):
    return render(request,"occasions1/Festival.html") 
def Party(request):
    return render(request,"occasions1/Party.html") 
def Embroidered(request):
    return render(request,"patterns1/Embroidered.html") 
def Solid(request):
    return render(request,"patterns1/Solid.html") 
def Printed(request):
    return render(request,"patterns1/Printed.html") 
def Stripes(request):
    return render(request,"patterns1/Stripes.html") 
def Floral(request):
    return render(request,"patterns1/Floral.html") 
def Checks(request):
    return render(request,"patterns1/Checks.html") 
def Ruffled(request):
    return render(request,"patterns1/Ruffled.html")                                                                                                                                           


# Create your views here.




