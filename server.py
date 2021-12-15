import socket
import threading


def main():
    host = "localhost"
    port = 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(2)

        player_contact = []
        players_threads = []

        print("Waiting for new connections...")
        connected = False
        while True:
            if not connected:
                if len(players_threads) < 2:
                    print(f"Active threads: {len(players_threads)}")

                    connection, client_address = server.accept()

                    new_client = threading.Thread(
                        group=None, target=get_clients_info, name=None,
                        args=(connection, player_contact), kwargs={}, daemon=None
                    )
                    players_threads.append(new_client)

                else:
                    print(f"Threads count:{len(players_threads)}")
                    for thread in players_threads:
                        thread.start()
                    connected = True

            # TODO: Game loop
            # 
            # send first cards with ui
            #
            # def choice
            #                     1. get 1 more card          2. Ready
            # (1) send 1 card to the player, then update information of second player about player 1's new card
            # (2) Next player

            # after dealer choice, send dealer card to players

            # again def choice 
            # if someone didnt loose after card pick, or just ready and have <= 21.
            # send game result

            # sart new game by sending new cards.

            

def send_first_cards(player_contact, game):
    pass


def game_choice(player_contact, game):
    pass
           

def get_clients_info(connection, player_contact):
    connection.send("Введите свое имя:".encode())
    client_name = connection.recv(1024).decode()
    player_contact.append({"conn": connection, "name": client_name})


if __name__ == "__main__":
    main()
