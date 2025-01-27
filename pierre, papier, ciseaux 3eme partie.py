import tkinter as tk
import random

# Initialiser la fenêtre du jeu
root = tk.Tk()
root.title("Jeu Pierre-Papier-Ciseaux")
root.geometry("400x400")
root.config(bg="lightblue")

# Titre du jeu
titre_label = tk.Label(root, text="Pierre-Papier-Ciseaux", font=("Arial", 20), bg="lightblue")
titre_label.pack(pady=20)

# Instruction
instruction_label = tk.Label(root, text="Choisissez Pierre, Papier ou Ciseaux :", font=("Arial", 14), bg="lightblue")
instruction_label.pack()

# Champ de saisie pour l'utilisateur
choix_utilisateur_var = tk.StringVar()
choix_utilisateur_entry = tk.Entry(root, textvariable=choix_utilisateur_var, font=("Arial", 14))
choix_utilisateur_entry.pack(pady=10)

# Champ de saisie pour afficher le résultat
Result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=Result, font=("Arial", 14), state='readonly', bg="lightgray")
result_entry.pack(pady=10)

# Fonction pour obtenir le choix de l'ordinateur
def choix_ordinateur():
    return random.choice(["pierre", "papier", "ciseaux"])

# Fonction pour gérer la logique du jeu
def play():
    choix_utilisateur = choix_utilisateur_var.get().lower()
    if choix_utilisateur not in ["pierre", "papier", "ciseaux"]:
        Result.set("Choisissez entre Pierre, Papier ou Ciseaux.")
        return
    
    comp_pick = choix_ordinateur()
    
    # Déterminer le résultat du jeu
    if choix_utilisateur == comp_pick:
        Result.set(f"L'ordinateur a choisi {comp_pick.capitalize()}. Égalité !")
    elif (choix_utilisateur == "pierre" and comp_pick == "ciseaux") or \
         (choix_utilisateur == "papier" and comp_pick == "pierre") or \
         (choix_utilisateur == "ciseaux" and comp_pick == "papier"):
        Result.set(f"L'ordinateur a choisi {comp_pick.capitalize()}. Vous gagnez !")
    else:
        Result.set(f"L'ordinateur a choisi {comp_pick.capitalize()}. L'ordinateur gagne !")

# Fonction pour réinitialiser le jeu
def Reset():
    choix_utilisateur_var.set("")  # Effacer le choix de l'utilisateur
    Result.set("")  # Réinitialiser le texte du résultat
    choix_utilisateur_entry.focus()  # Replacer le curseur dans le champ de saisie

# Fonction pour quitter l'application
def Exit():
    root.quit()

# Boutons pour jouer, réinitialiser et quitter
jouer_button = tk.Button(root, text="PLAY", font=("Arial", 14), command=play)
jouer_button.pack(pady=10)

reset_button = tk.Button(root, text="RESET", font=("Arial", 14), command=Reset)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="EXIT", font=("Arial", 14), command=Exit)
exit_button.pack(pady=10)

# Lancer la boucle principale tkinter
root.mainloop()
