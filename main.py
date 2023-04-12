import sys
import os
import signal
from my_gpt import ChatSession

def print_help():
    print("Commands:")
    print("  new <session_id> - Create a new chat session with the given ID.")
    print("  del <session_id> - Delete the chat session with the given ID.")
    print("  list - List all chat sessions.")
    print("  switch <session_id> - Switch to the specified chat session.")
    print("  help - Show this help message.")
    print("  quit - Quit the program.")
    print("To chat in a session, type '>' and your message.")

def main():
    sessions = {}
    active_session = None
    print("Welcome to the GPT-3 Chat CLI!")
    print_help()

    def signal_handler(signal, frame):
        print("\nExiting...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            if active_session is None:
                prompt = "> "
            else:
                prompt = f"{active_session}> "

            command = input(prompt).strip()

            if command == "quit":
                break
            elif command == "help":
                print_help()
            elif command.startswith("new "):
                session_id = command.split(" ")[1]
                if session_id in sessions:
                    print(f"Session with ID '{session_id}' already exists.")
                else:
                    sessions[session_id] = ChatSession()
                    active_session = session_id
                    print(f"Created new session: {session_id}")
                    print(f"Switched to session: {session_id}")
                    print(f"{active_session}> ", end="")
            elif command.startswith("del "):
                session_id = command.split(" ")[1]
                if session_id in sessions:
                    del sessions[session_id]
                    if active_session == session_id:
                        active_session = None
                        print(f"Deleted active session: {session_id}")
                    else:
                        print(f"Deleted session: {session_id}")
                else:
                    print(f"No session with ID '{session_id}' found.")
            elif command == "list":
                if len(sessions) == 0:
                    print("No active sessions.")
                else:
                    print("Active sessions:")
                    for session_id in sessions:
                        if session_id == active_session:
                            print(f"* {session_id}")
                        else:
                            print(f"  {session_id}")
            elif command.startswith("switch "):
                session_id = command.split(" ")[1]
                if session_id not in sessions:
                    print(f"No session with ID '{session_id}' found.")
                else:
                    active_session = session_id
                    print(f"Switched to session: {session_id}")
                    print(f"{active_session}> ", end="")
            elif active_session is not None:
                chat_session = sessions[active_session]
                answer = chat_session.ask_gpt3(command.strip())
                print(f"{active_session}(Assistant)> {answer}")
                num_messages = len(chat_session.messages)
                num_tokens = sum([chat_session.count_tokens(m["content"]) for m in chat_session.messages])
                print(f"Current session: {num_messages} messages, {num_tokens} tokens")
            else:
                print("No active session. Please create a new session using 'new <session_id>' command.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
