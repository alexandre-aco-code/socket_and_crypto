#if defined (WIN32)
    #include <winsock2.h>
    typedef int socklen_t;
#elif defined (linux)
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <unistd.h>
    #define INVALID_SOCKET -1
    #define SOCKET_ERROR -1
    #define closesocket(s) close(s)
    typedef int SOCKET;
    typedef struct sockaddr_in SOCKADDR_IN;
    typedef struct sockaddr SOCKADDR;
#endif
 
#include <stdio.h>
#include <stdlib.h>
#define PORT 6666
 
 
 
int main(void)
{
 
    SOCKET sock;
    SOCKADDR_IN sin;
    char buffer[32] = "";
 
    if(!erreur)
    {
        /* Création de la socket */
        sock = socket(AF_INET, SOCK_DGRAM, 0);
 
        /* Configuration de la connexion */
        sin.sin_addr.s_addr = inet_addr("127.0.0.1");
        sin.sin_family = AF_INET;
        sin.sin_port = htons(PORT);
 
        /* Si le client arrive à se connecter */
         printf("Connexion à %s sur le port %d\n", inet_ntoa(sin.sin_addr), htons(sin.sin_port));

         /* Si l'on reçoit des informations : on les affiche à l'écran */
         if(recvfrom(sock, buffer, 32, 0) != SOCKET_ERROR)
            printf("Recu : %s\n", buffer);
                
                
        /* On ferme la socket précédemment ouverte */
        closesocket(sock);
 
    }
 
    return EXIT_SUCCESS;
}