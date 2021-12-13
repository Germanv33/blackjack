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


def get_clients_info(connection, player_contact):
    connection.send("Введите свое имя:".encode())
    client_name = connection.recv(1024).decode()
    player_contact.append({"conn": connection, "name": client_name})


if name == "main":
    main()