import socket
import threading
from src.game import Game
from src.player import Player
import src.ui as UI

def main():
    host = "localhost"
    port = 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(2)

        player_contact = {}
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

<<<<<<< HEAD
            else:
                game = Game(player_contact[0]["name"], player_contact[1]["name"])
                
                # TODO: Game loop
                # 
                # send first cards with ui
                game.start_round()

                frst_conn = player_contact[0]["conn"]
                sec_conn = player_contact[1]["conn"]

                frst_conn.send(str(game).encode())
                sec_conn.send(str(game).encode())
                #
                # def choice
                #                     1. get 1 more card          2. Ready
                # (1) send 1 card to the player, then update information of second player about player 1's new card
                # (2) Next player

                player_1_turn = True

                if player_1_turn:
                    frst_conn.send(f"[Player 1's turn]".encode())
                    sec_conn.send(f"[Player 1's turn]".encode())
                    if frst_conn.recv(1024).decode() == "True":
                        if game.give_card(0):
                            continue
                    player_1_turn = False
                    player_2_turn = True
                    
                if player_2_turn:
                    frst_conn.send(f"[Player 2's turn]".encode())
                    sec_conn.send(f"[Player 2's turn]".encode())
                    if frst_conn.recv(1024).decode() == "True":
                        if game.give_card(1):
                            continue
                    player_2_turn = False
                
                if not (player_1_turn and player_2_turn):
                    if game.dealer_needs_buy():
                        connection.send("[Dealer's turn]".encode())
                        
                        game.give_card(2)
                    else:
                        connection.send("[End of round]".encode())
                        
                        if game.dealer_won():
                            connection.send(
                                "Sorry, you lost this time...".encode())
                        else:
                            connection.send("Nice! You won!".encode())
                        break



                # after dealer choice, send dealer card to players

                # again def choice 
                # if someone didnt loose after card pick, or just ready and have <= 21.
                # send game result

                # sart new game by sending new cards.

            

def send_first_cards(player_contact, game):

    game.start_round()

    frst_conn = player_contact[0]["conn"]
    sec_conn = player_contact[1]["conn"]

    frst_conn.send(str(game).encode())
    sec_conn.send(str(game).encode())
    
    return game



def game_choice(player_contact, game):
    
=======
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
>>>>>>> db2d54f0e5e610cc981f18cb86b0ff25ec02d342
           

def get_clients_info(connection, player_contact):
    connection.send("Введите свое имя:".encode())
    client_name = connection.recv(1024).decode()
    player_contact.append({"conn": connection, "name": client_name})


if __name__ == "__main__":
    main()
