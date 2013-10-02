from celery import task
from django.core import mail
from uchicagohvz.game.models import Kill
from uchicagohvz.users.phone import CARRIERS

@task
def send_death_notification(kill_id):
	kill = Kill.objects.get(id=kill_id)
	killer = kill.killer
	victim = kill.victim
	game = kill.killer.game
	players = game.players.filter(user__profile__phone_number__isnull=False, user__profile__subscribe_death_notifications=True)
	def gen_emails(): # email generator
		subject = "UChicago HvZ - death notification"
		victim_dorm = victim.dorm
		victim_dorm_name = victim.get_dorm_display()
		players_in_dorm = game.get_players_in_dorm(victim_dorm)
		body = "A human from %s was killed by %s. %s/%s humans from %s remain."
		body = body % (victim_dorm_name, killer.bite_code, players_in_dorm.filter(human=True).count(), players_in_dorm.count(), victim_dorm_name)
		for player in players:
			phone_number = player.user.profile.phone_number.replace('-', '')
			to_addr = CARRIERS[player.user.profile.phone_carrier] % (phone_number)
			email = mail.EmailMessage(subject=subject, body=body, to=[to_addr])
			yield email
	conn = mail.get_connection()
	conn.send_messages(tuple(gen_emails()))
