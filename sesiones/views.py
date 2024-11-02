from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_superuser
# Create your views here.

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request,'registro/registro.html',{'form':form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()

            login(request, usuario)
            return redirect('index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'registro/registro.html',{'form':form})
            

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def iniciar_sesion(request):
    if request.method=='POST':
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario_nom=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario = authenticate(username=usuario_nom, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                if User.is_superuser == True:
                    return redirect('principal')
                elif User.is_authenticated:
                    return redirect('index')
                
                
                
            
            else:
                form = AuthenticationForm(request)
                messages.error(request, 'usuario o contraseña no validos')
        
        else:
            form = AuthenticationForm(request)
            messages.error(request, 'credenciales no validas')
            return render(request, 'registro/login.html', {'form':form})
    
    form = AuthenticationForm()
    
    return render(request, 'registro/login.html', {'form':form})



@login_required
@user_passes_test(is_admin)
def lista_usuarios(request):
    users = User.objects.all()
    return render(request, 'ausuarios/adminusuario.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def usuarioAdd(request):
    context ={}
    
    if request.method == "POST":
        opcion = request.POST["opcion"]
        print(opcion)
        
        if opcion == "Añadir Usuario":
            print("Opcion: "+opcion)
            try:                
                usuario = request.POST["usuario"]
                email = request.POST["email"]                
                contra = request.POST["contra"]
                recontra = request.POST["recontra"]
                
                if contra == recontra:
                    newuser = User.objects.create_user(username=usuario, email=email, password=contra)
                    print(usuario, email)
                    newuser.save()
                    users = User.objects.all() 
                    context={'users': users,'ac':'El usuario ha sido agregado correctamente'}
                    return render(request, 'ausuarios/adminusuario.html', context)
            
            except:
                context={'ac2':'No se pudo agregar el usuario'}
                return render(request, 'ausuarios/usuarioAdd.html', context)
        
        if opcion == "Editar Usuario":
            
            users = User.objects.all()            
            context = {'users': users}
            return render(request, 'ausuarios/adminusuario.html', context)
        
        if opcion == "Actualizar":
            print("Entró a actualizar")
            print("Opción="+opcion)
            usuario = request.POST["usuario"]
            email = request.POST["email"]                
            contra = request.POST["contra"]
            
            usuariomod = User.objects.get(username=usuario)
            usuariomod.email=email
            usuariomod.set_password(contra)       
            
            usuariomod.save()

            users = User.objects.all()  
            context={'users': users,"ac":"Bien, datos actualizados"}

            return render(request,'ausuarios/usuarioAdd.html',context)
        
    return render(request, 'ausuarios/usuarioAdd.html', context)

@login_required
@user_passes_test(is_admin)
def usuarioEdit(request,pk):
    print("Hola estoy en UEdit", pk)
    context={}
    actuser = User.objects.get(username=pk)
               
    context={"usuario":actuser}
    
    print("salió del for")
    return render(request,'ausuarios/usuarioEdit.html',context)

@login_required
@user_passes_test(is_admin)
def usuarioDel(request, pk):
    
    try:
        eusuario = User.objects.get(username=pk)
        nom= eusuario.username
        
        eusuario.delete()
        

        users = User.objects.all()  
        context={'users': users,'ac':'Usuario ('+str(nom)+') eliminado correctamente'}
        
        return render(request, 'ausuarios/adminusuario.html', context)
    except:
        users = User.objects.all()  
        context = {'ac2':'No se pudo eliminar usuario ('+str(nom)+')', "users": users}
        return render(request, 'ausuarios/adminusuario.html', context)
    
