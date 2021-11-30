import sys
import random
import pygame.font
from time import sleep
import pygame
from source.settings import Settings
from source.game_stats import GameStats
from source.ship import Ship
from source.bullet import Bullet
from source.alien import Alien, Alien_Bullet, Alien_sniper_bullet
from source.button import Button


class AlienInvasion:
    # GamePlay and Class
    def __init__(self):
        # initialization
        pygame.init()
        self.start_ticks = pygame.time.get_ticks()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load("resource/images/background.png").convert()
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        pygame.mixer.music.load("resource/sound/game_music.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.bullet_sound = pygame.mixer.Sound("resource/sound/bullet.wav")
        self.bullet_sound.set_volume(0.2)

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.clock = pygame.time.Clock()

        self.fps = 60

        # create button
        self.play_button = Button(self, 'Play')

    def run_game(self):
        # main
        while True:
            # self.clock.tick(self.fps)
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # keyboard and mouse monitor and feedback
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.alien_bullets.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_z:
            self._fire_bullet()
        elif event.key == pygame.K_LSHIFT:
            self.settings.ship_speed = 0.2

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LSHIFT:
            self.settings.ship_speed = 0.5

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_sound.play()

    def _update_bullets(self):  # update the position of bullets and delete bullet that is off screen
        # update the position
        self.bullets.update()
        self.alien_bullets.update()
        # delete bullets that are off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        for bullet in self.alien_bullets.copy():
            if bullet.rect.bottom >= 700:
                self.alien_bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # check if collision takes place
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        self._create_fleet()
        if collisions:
            self.stats.game_score += 100
            print(self.stats.game_score)
        for bullet in self.alien_bullets:
            if pygame.sprite.collide_rect(bullet, self.ship.graze_box) and not bullet.grazed:
                self.stats.game_score += 100
                bullet.grazed = True
                print(self.stats.game_score)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.alien_bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.stats.game_active = False

    # def _check_aliens_bottom(self):
    #     screen_rect = self.screen.get_rect()
    #     for alien in self.aliens.sprites():
    #         if alien.rect.bottom >= screen_rect.bottom:
    #             self._ship_hit()
    #             break

    def _update_aliens(self):
        # self._check_fleet_edges()
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.bottom - alien.rect.height > self.screen.get_rect().bottom:
                self.aliens.remove(alien)
        if (pygame.time.get_ticks() - self.start_ticks) % 1000 == 0:
            for alien in self.aliens.copy():
                new_bullet = Alien_sniper_bullet(self, alien)
                self.alien_bullets.add(new_bullet)

        if pygame.sprite.spritecollideany(self.ship, self.aliens) or pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()

        # self._check_aliens_bottom()

    def _create_fleet(self):
        if self.stats.game_score <= 2000:
            if len(self.aliens) <= 10:
                self._create_alien()
        elif self.stats.game_score <= 5000:
            if len(self.aliens) <= 20:
                self._create_alien()
        else:
            # Boss fight
            pass

        # alien_width, alien_height = alien.rect.size
        # available_space_x = self.settings.screen_width - 2 * alien_width
        # number_aliens_x = available_space_x//(2 * alien_width)
        #
        # ship_height = self.ship.rect.height
        # available_space_y = (self.settings.screen_height - (4 * alien_height) - 2 * ship_height)
        # number_rows = available_space_y // (2 * alien_height)
        #
        # for row_number in range(number_rows):
        #     for alien_number in range(number_aliens_x):
        #         self._create_alien(alien_number, row_number)

    def _create_alien(self):
        # for i in range(alien_number):
        alien = Alien(self)
        alien.x = random.randint(0, self.screen_rect.right-alien.rect.width)
        alien.rect.x = alien.x
        # alien.rect.y = -500
        self.aliens.add(alien)


    # def _check_fleet_edges(self):
    #     for alien in self.aliens.sprites():
    #         if alien.check_edges():
    #             self._change_fleet_direction()
    #             break

    # def _change_fleet_direction(self):
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.settings.fleet_drop_speed
    #     self.settings.fleet_direction *= -1

    def _blite_gamescore(self):# under development
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render('Score:' + str(self.stats.game_score),True,(0,0,0))
        self.screen.blit(self.text,(0,0))

    def _update_screen(self):
        # draw stuff
        self.screen.blit(self.background, (0, 0))

        self.ship.bliteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self._blite_gamescore()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # make drawn stuff visible
        pygame.display.flip()


if __name__ == '__main__':
    # test and run
    ai = AlienInvasion()
    ai.run_game()

