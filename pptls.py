def determinate_winner(play:tuple):
    '''return the winner from a play'''
    plays={
        ("🗿", "✂️"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("✂️", "📄"): "Player 1",
        ("📄", "✂️"): "Player 2",
        ("📄", "🗿"): "Player 1",
        ("🗿", "📄"): "Player 2",
        ("🗿", "🦎"): "Player 1",
        ("🦎", "🗿"): "Player 2",
        ("🦎", "✂️"): "Player 1",
        ("✂️", "🦎"): "Player 2",
        ("✂️", "🖖"): "Player 1",
        ("🖖", "✂️"): "Player 2",
        ("🖖", "📄"): "Player 1",
        ("📄", "🖖"): "Player 2",
        ("📄", "🦎"): "Player 1",
        ("🦎", "📄"): "Player 2",
        ("🦎", "🗿"): "Player 1",
        ("🗿", "🦎"): "Player 2",
        ("🗿", "🖖"): "Player 1",
        ("🖖", "🗿"): "Player 2",
        ("🖖", "🦎"): "Player 1",
        ("🦎", "🖖"): "Player 2",
    }
    if play in plays:
        return plays[play]
    elif play[0]==play[1]:
        return "Tie"
    raise ValueError

def who_wins_more(plays:list[tuple]):
    player1_wins=[]
    player2_wins=[]
    ties=[]
    for play in plays:
        try:
            winner=determinate_winner(play)
            player1_wins.append(winner) if winner=='Player 1' else player2_wins.append(winner) if winner== 'Player 2' else ties.append(winner)
        except ValueError:
            print(f'la jugada {play} no es valida')
    result='El jugador que mas gano fue Player 1' if len(player1_wins)>len(player2_wins) and len(player1_wins)>len(ties) else 'El jugador que gano mas veces fue Player 2' if len(player2_wins)>len(player1_wins) and len(player2_wins)>len(ties) else 'la mayoria de jugadas fueron empate' if len(ties)>len(player2_wins) and len(ties)>len(player1_wins) else 'Player 1 Player 2 y los empates fueron los mismos'
    print(result)
    
who_wins_more([("🗿","✂️"), ("4","4","3"), ("📄","✂️")])