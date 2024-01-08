from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import status
from django.contrib.auth.models import User



class CustomLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Credenciais inválidas'}, status=400)

    def get(self, request):
        token = get_token(request)
        return JsonResponse({'csrf_token': token})
    
class CustomSignupView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Nome de usuário e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Nome de usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)

        if user:
            token = get_token(request)
            return Response({'success': 'Usuário criado com sucesso', 'csrf_token': token}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Falha ao criar usuário'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)