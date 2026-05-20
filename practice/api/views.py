from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'Dostep przyznany (JWT OK)!'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT) 
    # Dlaczego status 205 Reset Content a nie 200 OK?
    # Bo 205 Reset Content jest bardziej semantyczny przy operacji wylogowania: oznacza, 
    # że żądanie zakończyło się sukcesem, a klient powinien zresetować widok/formularz. 
    # 200 OK też by działało, ale 205 dokładniej przekazuje intencję „zakończ sesję i oczyść stan po stronie klienta”.
    except Exception as e:
        return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    

# * Czy endpoint powinien wymagać **`IsAuthenticated`**?
# Access Token wygasa szybciej Refresh Token co moze spowodować, ze uzytkownik nie bedzie mogl sie zalogowac bo bez access tokena IsAuthenticated nie przepuści i wywali błąd.
# Jest to dodatkowa warstwa zabezpieczenia więc edpoint moze wymagać IsAuthenticated ale nie musi.
   
# * Co w logach chcesz zapisać (bezpieczeństwo vs. PII)?
# Odp. Nie mozna logować wrazliwych danych takich jak tokeny, dane osobowe, hasła. Można logować informacje o błędach, adresy IP, 
# timestampy, ale bez danych umożliwiających identyfikację użytkownika. Logi powinny być anonimowe i nie zawierać PII (Personally Identifiable Information) ze względów bezpieczeństwa i prywatności.