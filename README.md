Bowling Game – 3D Bowling Simulation in Python & OpenGL

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Description
Bowling Game is a visually engaging 3D bowling simulation developed using Python, PyOpenGL, and Pygame. It supports two-player gameplay with a scoring system that accounts for strikes, spares, and frame-by-frame scoring. The game concludes with a "Game Over" screen displaying both players' final scores and offers the option to play again or exit.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features
  Two-player mode: The game alternates between two players, tracking scores individually across frames.
  Multiple lanes: Lanes are drawn in a 3D OpenGL environment using geometric functions like draw_lane1() to draw_lane7() and Triangle() for pins.
  Dynamic ball control: Players control the ball direction using arrow keys and launch with the space bar.
  Pin collision & scoring: The ball can knock down pins, triggering scoring updates. It handles strikes (all pins in one throw) and spares (all pins in two throws).
  Score tracking per frame: The game maintains frame-by-frame scoring for both players, updating scores based on pin hits.
  Game end & prompt: After two frames for each player, it displays a GAME OVER message showing both players’ final scores, and prompts to restart or quit.
  Sound integration:
    Background bowling center ambience plays when the game starts, creating a realistic environment.
    Strike/hit sound effect plays when the ball hits the pins, enhancing the gameplay feedback.
  Replay option: After the game ends, players can choose to play again by pressing 'Y' or exit with 'N'.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Technologies Used
Python 3.x
PyOpenGL
Pygame
OpenGL (GL, GLU)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Full code for main() is available in the source and demonstrates integration of graphics, controls, state management, and audio.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main() function : initializes the OpenGL window, loads textures, sets up lanes and pins, and runs the main game loop. It tracks:
  Ball position and motion (ball_x, ball_z)
  Pin collisions and states
  Throw counts (for determining second attempts in a frame)
  Turn switching between Player 1 and Player 2
  Frame completion and scoring updates
  Game over detection after 2 frames each


if frame_count[0] == 2 and frame_count[1] == 2 :
    if show_game_over and time.time() >= game_over_time:
        game_over = True
        player_1 = True
        player_2 = True

Scoring System :
  Strike: Knocking all pins on first throw – next two throws count as bonus.
  Spare: Knocking all pins in two throws – next throw counts as bonus.
  Score is updated with:

update_score(pins_hit_count) :
  total_score_p1 += score_turn1 + score_turn2
  total_score_p2 += score_turn1 + score_turn2

Lanes and Pins :
  Custom drawing functions render 3D lanes and triangular pins using OpenGL primitives (Triangle() and draw_laneX() calls). Each pin position is defined, and     
  collisions are checked during ball movement.

Game Reset / Play Again :
  After the game ends:
    A final score screen is shown.
    The player is prompted to press Y to play again or N to exit.


if play_again_prompt_time != 0 and time.time() >= play_again_prompt_time :
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        restart_game = True
    elif keys[pygame.K_n]:
        pygame.quit()
        exit()

Controls :
  Left/Right Arrow Keys – Move the ball before launch
  Space Bar – Launch the ball
  Y/N Keys – Choose to play again or quit after game over

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Learning Goals :
  Learn OpenGL 3D rendering with Python
  Implement game state machines (turns, scores, resets)
  Manage user inputs and animations in a loop
  Apply basic collision detection logic

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Future Improvements :
  Frame-by-frame score display
  Realistic physics for spin, bounce
  Multiple camera angles
  Sound effects for pin collisions and strike/spare
  Scoreboard UI overlay

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

License :
This project is open-source and available under the MIT License.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
