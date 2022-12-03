from django.db import models

# Create your models here.
# Django ORM
class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    initial_price = models.FloatField(verbose_name='Preço inicial')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

class MyTeam(models.Model):
    players = models.ManyToManyField(Player, verbose_name='Jogadores')

    def __str__(self):
        return [player.name for player in self.players.all()].__str__()
    
    class Meta:
        verbose_name = 'Meu time'
        verbose_name_plural = 'Meus times'


class Match(models.Model):
    match_date = models.DateTimeField(verbose_name='Data do jogo')
    team_a = models.ForeignKey(
        Team, 
        on_delete=models.PROTECT, 
        related_name='team_a_matches', 
        verbose_name='Time A'
    )
    team_a_goal = models.IntegerField(default=0, verbose_name='Gols do time A')
    team_b = models.ForeignKey(
        Team, 
        on_delete=models.PROTECT, 
        related_name='team_b_matches', 
        verbose_name='Time B'
    )
    team_b_goal = models.IntegerField(default=0, verbose_name='Gols do time B')

    def __str__(self):
        return f'{self.team_a} x {self.team_b}'
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

class Action(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, verbose_name='Jogador')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name='Time')
    minutes = models.IntegerField(verbose_name='Minutos')
    match = models.ForeignKey(Match, on_delete=models.PROTECT, verbose_name='Jogo')

    class Actions(models.TextChoices):
        GOAL = 'goal', 'Gol'
        ASSIST = 'assist', 'Assistência'
        YELLOW_CARD = 'yellow card', 'Cartão amarelo'
        RED_CARD = 'red card', 'Cartão vermelho'
    
    action = models.CharField(max_length=50, choices=Actions.choices, verbose_name='Ação')

    def __str__(self):
        return f'{self.player} - {self.action}'

    class Meta:
        verbose_name = 'Ação do jogo'
        verbose_name_plural = 'Ações do jogo'

## SQL
# create table match (match_date datetime, team_a_id int) ON delete 