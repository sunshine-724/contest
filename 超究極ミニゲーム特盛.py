import pygame as pg
from pygame.locals import *
import random
from random import randint,randrange
import copy
pg.init()
screen_width=1280
screen_height=720
black_line_y = pg.display.Info().current_h
# screen=pg.display.set_mode((screen_width,screen_height))
# screen=pg.display.set_mode((screen_width,screen_height),FULLSCREEN)
# screen=pg.display.set_mode((screen_width,screen_height),pg.FULLSCREEN | pg.SCALED)
screen=pg.display.set_mode((screen_width,screen_height),RESIZABLE)
# screen=pg.display.set_mode((screen_width,screen_height),pg.RESIZABLE | pg.SCALED)
pg.display.set_caption("超究極ミニゲーム奇跡")
home_x=0
home_y=0
white=(255,255,255)
screen.fill(white)
home_unit=("秒","ミス","貫","個")
home_modo=[[False,"???"] for i in range(len(home_unit))]
home_bestscore=["-" for i in range(len(home_modo))]
home_clearcount=[0 for i in range(4)]
home_manual=tuple(pg.image.load("assets/home/manual/"+i+".png") for i in ("sakana","okasinoie","pakuttosalmon","pankuiUFO"))
home_font="assets/font/GenEiGothicN-Heavy.otf"
home_screen=pg.image.load("assets/home//picture/home_ui.png")
home_delete=pg.image.load("assets/delete/background.png")
home_delete_choice=pg.image.load("assets/delete/cursor.png")
home_frame=tuple(pg.image.load("assets/home/picture/select_"+i+".png") for i in ("1","2","3"))
home_package=tuple(pg.image.load("assets/home/package/"+i+".png") for i in ("sakana","okasinoie","pakuttosalmon","pankuiUFO"))
home_mouse_x=0
home_mouse_y=0
home_click=False
home_clock=pg.time.Clock()
home_fps=60
home_scene=0
home_run=True
home_se_choose=pg.mixer.Sound("assets/home/sound/select.mp3")
home_se_mistake=pg.mixer.Sound("assets/home/sound/miss.mp3")
home_se_decision=pg.mixer.Sound("assets/home/sound/go.mp3")
home_se_back=pg.mixer.Sound("assets/home/sound/back.mp3")
#星
# [[0,"ピッカピカ","「ワイプ・ザ・ウィンドウ」をクリアする"],[0,"きれい好き","「ワイプ・ザ・ウィンドウ」を5回クリアする"],[0,"大掃除","「ワイプ・ザ・ウィンドウ」を7回クリアする"],[0,"右大臣","？？？（スター“きれい好き”を獲得したら獲得条件がわかるよ）"],[0,"大失敗","？？？"],[0,"破壊神","？？？"],[0,"ヒント","スター“大掃除”を獲得たらヒントが見れるよ"]],
star_liset=[[[0,"ミッケ！","「魚」をクリアする"],[0,"大漁","「魚」を5回クリアする"],[0,"探偵","「魚」を70秒以内にクリアする"],[0,"探し物名人","「魚」を30秒以内にクリアする"],[0,"鯛","「魚」で“鯛”に遭遇する"],[0,"鯖","「魚」で“鯖”に遭遇する"],[0,"ヒント","スター“大漁”を獲得するしたらヒントが見れるよ"]],
            [[0,"ピッカピカ","？？？"],[0,"きれい好き","？？？"],[0,"大掃除","？？？"],[0,"右大臣","？？？（スター“きれい好き”を獲得したら獲得条件がわかるよ）"],[0,"大失敗","？？？"],[0,"破壊神","？？？（スター“右大臣”を獲得したら獲得条件がわかるよ）"],[0,"拭け！","？？？（スター“大掃除”を獲得したら獲得条件がわかるよ）"],[0,"ヒント","スター“大掃除”を獲得たらヒントが見れるよ"]],
            [[0,"おいしい","「パクッとサーモン」をクリアする"],[0,"行きつけのお店","「パクッとサーモン」を5回以上クリアする"],[0,"常連さん","「パクッとサーモン」を10回以上クリアする"],[0,"大食い","「パクッとサーモン」を200貫以上食べてクリアする"],[0,"フードファイター","「パクッとサーモン」を300貫以上食べてクリアする"],[0,"サーモンフェア","「パクッとサーモン」をトリプルサーモン食べてクリアする"],[0,"ヒント","スター“常連さん”を獲得したらヒントが見れるよ"]],
            [[0,"初心者パイロット","「パン食いUFO」をクリアする"],[0,"中堅パイロット","「パン食いUFO」を5回クリアする"],[0,"ベテランパイロット","「パン食いUFO」を7回クリアする"],[0,"長時間フライト","「パン食いUFO」でパン3斤分長く飛ぶ"],[0,"パンマニア","「パン食いUFO」でジャムを30個以上回収してクリアする"],[0,"パン王","「パン食いUFO」でジャムを40個以上回収してクリアする"],[0,"ヒント","スター“ベテランパイロット”を獲得したらヒントが見れるよ"]]]
star=copy.deepcopy(star_liset)
fontsize_home_star=45
font_home_star=pg.font.Font(home_font,fontsize_home_star)
fontsize_home_star_game_name=44
font_home_star_game_name=pg.font.Font(home_font,fontsize_home_star_game_name)
star_background=pg.image.load("assets/star/background.png")
star_screen=pg.image.load("assets/star/ui.png")
star_cleared=pg.image.load("assets/star/star.png")
star_notcleared=pg.image.load("assets/star/nostar.png")
star_light=pg.image.load("assets/star/hint.png")
str_se_choice=pg.mixer.Sound("assets/star/select.mp3")
star_x=0
star_y=0
star_game_name=("魚","お菓子の家","パクッとサーモン","パン食いUFO")
star_hint=("目を細めて少し遠くから見てみよう","気合をいれろ","気を抜くな","キーボードを回して操作してみよう")
star_clearrate=0
star_clearcount=0
star_count=0
for i in range(len(star)):
    star_count+=len(star[i])-1
stop_button=pg.image.load("assets/home/manual/stop_button.png")
manual_mode=2

def fish():
    se_fail=pg.mixer.Sound("assets/fish/sound/false.mp3")
    se_clea=pg.mixer.Sound("assets/fish/sound/clear.mp3")
    se_search=pg.mixer.Sound("assets/fish/sound/search.wav")
    se_explosion=pg.mixer.Sound("assets/fish/sound/explosion.mp3")
    se_gun=pg.mixer.Sound("assets/fish/sound/shot.mp3")
    frame=pg.image.load("assets/fish/picture/flame.png")
    mousecursor=pg.image.load("assets/fish/picture/mousecursor.png")
    triangle=pg.image.load("assets/fish/picture/triangle.png")
    pg.mixer.music.load("assets/fish/sound/bgm.wav")
    pg.mixer.music.play(loops=-1)
    mouse_x=0#mx
    mouse_y=0
    lottery=0
    colmuns=11
    rows=6
    fontsize=82
    interval=12
    font_fish = pg.font.Font("assets/font/keifont.ttf",fontsize)
    font_score = pg.font.Font("assets/font/GenEiGothicN-SemiBold.otf",40)
    font_GAMECLEAR=pg.font.Font("assets/font/GenEiGothicN-SemiBold.otf",120)
    lottety_x = random.randint(0,colmuns-1)
    lottety_y = random.randint(0,rows-1)
    chosen_x=0
    chosen_y=0
    score=100
    clearcount=0
    clear=-1
    starttime=pg.time.get_ticks()
    rare1_flag=False
    rare2_flag=False
    support=3
    search=False
    volume=1
    wait=False
    explosion=False
    topright=tuple(pg.image.load("assets/fish/picture/happy_"+str(i)+".png") for i in range(9))
    if random.randrange(2)==1:
        explosion=True
        support=2
        swich=tuple(pg.image.load("assets/fish/picture/explosion_"+i+".png") for i in ("green","red","gray"))
    else:
        swich=tuple(pg.image.load("assets/fish/picture/search_"+i+".png") for i in ("green","red","gray"))
    delete_l=[-50 for i in range(8)]
    delete__=[-50 for i in range(5)]
    GAMECLEAR=["GAMECLEAR"]
    happy_fps=60
    left_limit=95
    up_limit=125
    normal="鮭"
    enemy="鮪"
    rare1="鯛"
    rare2="鯖"
    fish_stop_button_x=875
    fish_stop_button=pg.transform.scale(stop_button,(1700//6.5,472//6.5))
    manual_time=0
    if on_manual(0):
        fish_on_manual=True
    else:
        fish_on_manual=False
    run=True
    if home_modo[0][0]:
        rows=8
        colmuns=16
        normal="鮎"
        enemy="鯉"
        rare1="鰻"
        rare2="鯨"
        fontsize=63
        interval=8
        left_limit=40
        up_limit=110
        support+=1
        font_fish = pg.font.Font("assets/font/LightNovelPOPv2.otf",fontsize)
    fontsize_and_interval=fontsize+interval
 
    while run:
        screen.fill(white)
        mouse_x,mouse_y=pg.mouse.get_pos()
        if mouse_y>=671:
             triangley=670
        elif mouse_y>=126:
            triangley=mouse_y
        else:
             triangley=126
        if clearcount<8:
            time=pg.time.get_ticks()-starttime
        if clearcount==8 and (clear<=0):
            clear=0
            if  home_clearcount[0]==0 or home_bestscore[0]>time/1000:
                home_bestscore[0]=time/1000
            home_clearcount[0]+=1
            star[0][0][0]=1
            se_clea.play()
            if home_clearcount[0]>=5:
                star[0][1][0]=1
                star[0][len(star[0])-1][2]=star_hint[0]
            if time<=70000:
                star[0][2][0]=1
                if time<=30000:
                    star[0][3][0]=1
        if clear>=0:
            screen.blit(font_GAMECLEAR.render(GAMECLEAR[0][0:clear], True, (0,0,0)),(260,300))
            # screen.blit(font_GAMECLEAR.render(GAMECLEAR[0][0:(clearcount-8)*10], True, (0,0,0)),(260,300))
            screen.blit(font_score.render("Rキー：戻る", True, (0,0,0)),(80,650))
            if clear<9:
                 clear+=1
                 pg.time.delay(50)

                 

             

        for i in range(colmuns):
            if not i in delete_l:
                for a in range(rows):
                    if  i==lottety_x and a==lottety_y and clearcount<8 and not a in delete__:
                        if rare1_flag==True:
                            screen.blit(font_fish.render(rare1, True, (0,0,0)),(left_limit+fontsize_and_interval*i,up_limit+fontsize_and_interval*a))
                        elif rare2_flag:
                            screen.blit(font_fish.render(rare2, True, (0,0,0)),(left_limit+fontsize_and_interval*i,up_limit+fontsize_and_interval*a))
                        else:
                            screen.blit(font_fish.render(enemy, True, (0,0,0)),(left_limit+fontsize_and_interval*i,up_limit+fontsize_and_interval*a))
                    elif clearcount<8 and not a in delete__ :
                        screen.blit(font_fish.render(normal, True, (0,0,0)),(left_limit+fontsize_and_interval*i,up_limit+fontsize_and_interval*a))

        if search:
            volume=1-0.6*(abs(4+fontsize_and_interval*lottety_x-mouse_x)/1230)-0.4*(abs(89+(fontsize+interval)*lottety_y-mouse_y)/598)
            se_search.set_volume(volume)
            
        for event in pg.event.get():
                global home_scene
                if event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3):
                    if clearcount<8 and mouse_y>=up_limit-12:
                        chosen_x=(mouse_x-left_limit)//fontsize_and_interval
                        chosen_y=(mouse_y-up_limit)//fontsize_and_interval
                        if chosen_x==lottety_x and chosen_y==lottety_y :
                            score+=100
                            lottety_x = random.randint(0,colmuns-1)
                            lottety_y = random.randint(0,rows-1)
                            delete_l=[-50 for i in range(8)]
                            delete__=[-50 for i in range(5)]
                            search=False
                            se_search.stop()
                            se_gun.play()
                            clearcount+=1
                            rare1_flag=False
                            rare2_flag=False
                            screen.fill(white)
                            wait=True
                            if home_clearcount[0]>0:
                                lottery=random.randint(1,20)
                                if lottery==1:
                                    rare1_flag=True
                                    star[0][4][0]=1
                                elif lottery==2:
                                    rare2_flag=True
                                    star[0][5][0]=1
                        else:
                            starttime-=2000
                            se_fail.play()
                    elif fish_on_manual and mouse_y < 68 and fish_stop_button_x<mouse_x<1125:
                        manual_time=pg.time.get_ticks()
                        screen.blit(triangle,(1215,triangley))
                        screen.blit(mousecursor,(mouse_x-23,mouse_y-23))
                        pg.draw.rect(screen,(0,0,0), (1240,0,100,720))
                        pg.draw.rect(screen,(255,169,49), (1240,660-66*clearcount,100,795))
                        screen.blit(topright[clearcount],(1146,0))
                        if support>1:
                            screen.blit(swich[0],(425,0))
                        elif support==1:
                            screen.blit(swich[1],(425,0))
                        else:
                            screen.blit(swich[2],(425,0))
                        screen.blit(frame,(0,0))
                        screen.blit(font_score.render(str(time/1000), True, (255,0,0)),(20,10))
                        manual()
                        starttime+=pg.time.get_ticks()-manual_time
                    elif clearcount>8:
                        home_scene=0
                        se_search.stop()
                        run=False
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                        home_scene=0
                        se_search.stop()
                        run=False
                if ((event.type == pg.KEYDOWN and event.key == pg.K_SPACE) or(event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and mouse_y<=up_limit-30 and 420<mouse_x<860) ) and support>0 and search==False and delete__[0]==-50:
                        if explosion:
                            se_explosion.play()
                            support-=1
                            delete_l=random.sample(range(colmuns+1),8)
                            delete__=random.sample(range(rows+1),5)
                            if lottety_x in delete_l:
                                delete_l.remove(lottety_x)
                            else:
                                delete_l.pop(-1)
                            if lottety_y in delete__:
                                delete__.remove(lottety_y)
                            else:
                                delete__.pop(-1)
                        else:
                            support-=1
                            search=True
                            se_search.play(loops=-1)
        screen.blit(triangle,(1215,triangley))
        screen.blit(mousecursor,(mouse_x-23,mouse_y-23))
        # screen.blit(font_score.render(str(clearcount//10)+"/8回", True, (0,0,0)),(1000,10))
        pg.draw.rect(screen,(0,0,0), (1240,0,100,720))
        pg.draw.rect(screen,(255,169,49), (1240,660-66*clearcount,100,795))
        screen.blit(topright[int(clearcount)],(1146,0))
        if support>1:
            screen.blit(swich[0],(425,0))
        elif support==1:
            screen.blit(swich[1],(425,0))
        else:
            screen.blit(swich[2],(425,0))
        screen.blit(frame,(0,0))
        screen.blit(font_score.render(str(time/1000), True, (255,0,0)),(20,10))
        if fish_on_manual:
            screen.blit(fish_stop_button,(fish_stop_button_x,5))

        pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))
        pg.display.update()
        if wait:
            pg.time.delay(100)
            wait=False
        home_clock.tick(happy_fps)
def window():
    flame_color=(223,153,0)
    flame_flame_color=(93,54,5)
    dustcloth=pg.transform.rotate(pg.transform.scale(pg.image.load("assets/window/picture/dustcloth.png"), (int(2160//5), int(1620//5))), 110)
    if home_modo[1][0]:
        dustcloth=pg.image.load("assets/window/picture/dustcloth.png")
        flame_color=(126,56,0)
        flame_flame_color=(67,37,0)
        tree=pg.image.load("assets/window/picture/tree.png")
    light=pg.image.load("assets/window/picture/right.png")
    dustcloth_y=50
    dustcloth_x=800
    seigyo=0
    count=0
    font=pg.font.Font("assets/font/GenEiGothicN-SemiBold.otf",40)
    font_cleartime=pg.font.Font("assets/font/LightNovelPOPv2.otf",45)
    right=True
    miss=0
    breakcount=0
    time=pg.time.get_ticks()
    pg.mixer.music.load("assets/window/sound/bgm.wav")
    pg.mixer.music.play(loops=-1)
    wipethewindow_fps=60
    se_wipe1=pg.mixer.Sound("assets/window/sound/wipe_1.wav")
    se_wipe2=pg.mixer.Sound("assets/window/sound/wipe_2.wav")
    se_finish=pg.mixer.Sound("assets/window/sound/clear.mp3")
    se_break=pg.mixer.Sound("assets/window/sound/break.mp3")
    window_stop_button=pg.transform.scale(stop_button,(1700//6.5,472//6.5))
    mouse_x=0
    mouse_y=0
    if on_manual(1):
        window_on_manual=True
    else:
        window_on_manual=False
    run=True
    while run:
        if breakcount<=40:
            windowcolor=((2+173*count//70),62+162*count//70,79+149*count// 70)
            screen.fill(windowcolor)
        else:
            screen.fill(windowcolor)
            if home_modo[1][0]:
                screen.blit(tree,(0,0))
            screen.blit(font.render("Rキー：戻る", True, (175,224,248)),(90,600))
            screen.blit(font_cleartime.render(str(time/1000), True, (175,224,248)),(700,600))

        if count==70:
            if  home_clearcount[1]==0 or home_bestscore[1]>miss:
                home_bestscore[1]=miss
            home_clearcount[1]+=1
            star[1][0][0]=1
            star[1][0][2]="「お菓子の家」をクリアする"
            time=pg.time.get_ticks()-time
            if right:
                star[1][3][0]=1
                star[1][3][2]="「お菓子の家」を左クリックをせずにクリアする"
                star[1][5][2]="「お菓子の家」でクリアした後も連打する"
            if home_clearcount[1]>=5:
                star[1][1][0]=1
                star[1][1][2]="「お菓子の家」を5回クリアする"
                star[1][3][2]="「お菓子の家」を左クリックをせずにクリアする"
                if home_clearcount[1]>=7:
                    star[1][2][0]=1
                    star[1][2][2]="「お菓子の家」を7回クリアする"
                    star[1][6][2]="「お菓子の家」で窓を拭かずに戻る"
                    star[1][len(star[1])-1][2]=star_hint[1]
            if miss>=30:
               star[1][4][0]=1
               star[1][4][2]="「お菓子の家」で30回ミスをする"
            se_finish.play()
            count=71
        if count==71 and breakcount<=40:
            screen.blit(light,(10,0))
            screen.blit(font.render("Rキー：戻る", True, (237,253,255)),(90,600))
            screen.blit(font_cleartime.render(str(time/1000), True, (237,253,255)),(700,600))
            if breakcount==40:
                se_break.play()
                windowcolor=(255,255,255)
                star[1][5][0]=1
                star[1][5][2]="「お菓子の家」でクリアした後も連打する"
                breakcount=41

        pg.draw.rect(screen,(flame_flame_color), (0,0,1280,720),45) 
        pg.draw.line(screen,(flame_flame_color),(635,0),(635,720),width=50) 
        pg.draw.line(screen,(flame_color),(635,0),(635,720),width=40) 
        pg.draw.rect(screen,(flame_color), (0,0,1280,720),40) 
        if window_on_manual:
            screen.blit(window_stop_button,(1020,5))
        screen.blit(dustcloth,(dustcloth_x,dustcloth_y)) 
        for event in pg.event.get():
                global home_scene
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    if count<70:
                        if seigyo==1:
                            count+=1
                            seigyo=0
                            dustcloth_y=50
                            dustcloth_x=800 
                            se_wipe1.play()
                        else:
                            miss+=1
                    elif breakcount<40:
                        breakcount+=1
                elif event.type == MOUSEBUTTONDOWN :
                    mouse_x,mouse_y=pg.mouse.get_pos()
                    if 1020<=mouse_x and mouse_y<68 and window_on_manual:
                        manual()
                    elif count<70:
                        if seigyo==0:
                            if event.button==2 or event.button==1:
                                right=False
                            if event.button==1 or event.button==2 or event.button==3:
                                count+=1
                                seigyo=1
                                dustcloth_y=200
                                dustcloth_x=30 
                                se_wipe2.play()
                        else:
                                miss+=1
                    elif breakcount<40:
                        breakcount+=1
                    # elif breakcount==41:
                    #     home_scene=0
                    #     if count==0:
                    #         star[1][6][0]=1
                    #         star[1][6][2]="「ワイプ・ザ・ウィンドウ」で窓を拭かずに戻る"
                    #     run=False
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                        home_scene=0
                        if count==0:
                            star[1][6][0]=1
                            star[1][6][2]="「お菓子の家」で窓を拭かずに戻る"
                        run=False

        pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))
        pg.display.update()
        home_clock.tick(wipethewindow_fps)
def salmon():
    background=pg.image.load("assets/salmon/normal/background.png")
    picture=tuple(pg.image.load("assets/salmon/normal/"+i+".png") for i in ("salmon","salmon_w","salmon_goald","salmon_order_w","salmon_order","tuna","tuna_w","egg","salmon_triple"))
    cloud_picture=pg.image.load("assets/salmon/cloud.png")
    cloud_x=-755
    cloudcount=0
    cloud=False
    lottery=randrange(1,101)
    interval=300
    speed=18
    count=0
    list=[]
    pressedcolor=(255,221,119)
    money=2000001
    finish=False
    finished=False
    se=pg.mixer.Sound("assets/salmon/get.wav")
    se_finish=pg.mixer.Sound("assets/salmon/finish.wav")
    font_sara = pg.font.Font(home_font,100)
    font_count = pg.font.Font(home_font,180)
    font_back= pg.font.Font("assets/font/GenEiGothicN-SemiBold.otf",30)
    font_money=pg.font.Font(home_font,40)
    pg.mixer.music.load("assets/salmon/bgm.wav")
    pg.mixer.music.play(loops=-1)
    run=True
    salmon_fps=30
    salmon_stop_button=pg.transform.scale(stop_button,(1700//6.5,472//6.5))
    mouse_x=0
    mouse_y=0
    if home_modo[2][0]==True :
        background=pg.image.load("assets/salmon/burned/background.png")

        picture=tuple(pg.image.load("assets/salmon/burned/"+i+".png") for i in ("burnedsalmon","burnedsalmon_w","burnedsalmon_goald","hamburgersteak","burnedsalmon_order","tunaroll","cucumberroll","soup","burnedsalmon_triple"))
        interval=8
        speed=27
    sushi=[[-353,False,0,picture[0]] for i in range(5)]
    if on_manual(2):
        salmo_on_manual=True
    else:
        salmo_on_manual=False
    sushi[0][1]=True
        #X座標  表示　種類　画像   
    while run:
        screen.fill(white)
        pg.draw.rect(screen,(pressedcolor), (1000,460,280,200))
        screen.blit(background,(0,0))
        lottery=randrange(1000)
        screen.blit(font_sara.render("貫", True, (0,0,0)),(470,200))
        screen.blit(font_count.render(str(count), True, (0,0,0)),(130,140))
        screen.blit(font_back.render("Rキー：戻る", True, (255,255,255)),(30,660))
        screen.blit(font_money.render(str(money), True, (255,255,255)),(1060,25))
        if salmo_on_manual:
            screen.blit(salmon_stop_button,(1020,650))
        for i in range(len(sushi)):
            if sushi[i][1]==False and interval<sushi[i-1][0]<1000 and finish==False:
                sushi[i][1]=True
                if lottery>250:
                        if lottery>=950:
                            sushi[i][3]=picture[2]
                            sushi[i][2]=3
                        elif lottery>=948:
                            sushi[i][3]=picture[8]
                            sushi[i][2]=2
                        else:
                            sushi[i][2]=0
                            if lottery>600:
                                sushi[i][3]=picture[0]
                                sushi[i][2]=0
                            else:
                                sushi[i][3]=picture[1]
                                sushi[i][2]=4
                else: 
                    sushi[i][2]=1
                    if lottery>150:
                        sushi[i][3]=picture[5]
                    elif lottery>110:
                        sushi[i][3]=picture[6]
                    elif lottery>70:
                        sushi[i][3]=picture[7]
                    elif lottery>30:
                        sushi[i][3]=picture[3]
                    else:
                        sushi[i][3]=picture[4]

        for i in range(len(sushi)):
            if sushi[i][1]==True :
                screen.blit(sushi[i][3],(sushi[i][0],300))
                sushi[i][0]+=speed
            if sushi[i][0]>1280 :
                if sushi[i][2]==1 or sushi[i][2]==3:
                    sushi[i][0]=-338
                    sushi[i][1]=False
                elif sushi[i][2]==0 or sushi[i][2]==2 or sushi[i][2]==4:
                    finish=True    

        if interval>8 and home_modo[2][0]==False:
            interval=338-((count//2*8))
            if interval<8:
                interval=8            
        if speed<27 and home_modo[2][0]==False:
            speed=18+(count//5)
        if finish:
            finish=False
            cloud=False
            se_finish.play()
            for i in range(len(sushi)):
                sushi[i][1]=False
                sushi[i][0]=-338
            finished=True

        if cloud_x>-755:
            screen.blit(cloud_picture,(cloud_x,280))
            if cloud_x<-100 and cloud:
                cloud_x+=5
            if cloud==False:
                cloud_x-=5   
        pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))        
        pg.display.update()
        pressedcolor=(255,221,119)  
        for event in pg.event.get(): 
            mouse_x,mouse_y=pg.mouse.get_pos()
            if ((event.type==pg.KEYDOWN and event.key == pg.K_SPACE) or (event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3))) and finish==False and (1020 > mouse_x or 650 > mouse_y or salmo_on_manual==False):
                    for i in range(len(sushi)):
                        if 647<=sushi[i][0]:
                            list.append(i)
                    if not len(list)==0:
                        if len(list)>=2:
                            if abs(sushi[list[0]][0]-971)>abs(sushi[list[1]][0]-971):
                                del list[0]
                            else:
                                del list[1]
                        list=list[0]

                        if not sushi[list][2]==1:
                            sushi[list][1]=False
                            sushi[list][0]=-338
                            count+=1
                            cloudcount+=1
                            se.play()
                            if sushi[list][2]==3:
                                 money-=1000000
                            if  sushi[list][2]==2:
                                star[2][5][0]=1
                                count+=2
                            if sushi[list][2]==4:
                                count+=1
                            if money<=0:
                                finish=True
                            if count>100 and random.randrange(200)==0 and cloud==False:
                                cloud=True
                                cloudcount=0
                                cloud_x=-754
                            if cloudcount>20:
                                cloud=False
                        else:
                            finish=True
                            money=-9999999           
                        list=[]
                    pressedcolor=(255,100,100)

            if (event.type == pg.KEYDOWN and event.key == pg.K_r) or (finished and event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and (1020 > mouse_x or 650 > mouse_y or salmo_on_manual==False)):
                        global home_scene
                        home_scene=0
                        if home_clearcount[2]==0  or  home_bestscore[2]<count:
                            home_bestscore[2]=count
                        if count>0:
                            star[2][0][0]=1
                            home_clearcount[2]+=1
                        if home_clearcount[2]>=5:
                            star[2][1][0]=1
                            if home_clearcount[2]>=10:
                                star[2][2][0]=1
                                star[2][len(star[2])-1][2]=star_hint[2]
                        if count>=200:
                            star[2][3][0]=1
                            if count>=300:
                                 star[2][4][0]=1
                        run=False
            if event.type == pg.MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 1020 < mouse_x and 650 < mouse_y and salmo_on_manual:
                manual()

        home_clock.tick(salmon_fps)
def UFO():
    UFO_x=462
    UFO_y=303
    item=[[random.randrange(900),
          random.randrange(600),
          0,
          pg.time.get_ticks()-1500+(random.randrange(30)*100),
          random.randrange(1000)] for i in range(20)]
    #X座標,Y座標,表示,時間,種類
    direction=random.randrange(3)
    speed=0
    limit_x=924
    limit_y=720-(579//5)
    timeplus=pg.time.get_ticks()
    meter_y=0
    gemcount=0
    size=0
    fuel_count=0 
    se_last=pg.mixer.Sound("assets/UFO/sound/finish.mp3")
    se_jem=pg.mixer.Sound("assets/UFO/sound/jam.mp3")
    se_fuel=pg.mixer.Sound("assets/UFO/sound/bread.mp3")
    se_change=pg.mixer.Sound("assets/UFO/sound/rotate.mp3")
    pg.mixer.music.load("assets/UFO/sound/bgm.wav")
    pg.mixer.music.play(loops=-1)
    pushedkeycount=0
    pushedkey=(K_UP,K_RIGHT,K_DOWN,K_LEFT)
    arrow=tuple(pg.transform.rotate(pg.image.load("assets/UFO/arrow.png"),i) for i in (0,-90,180))
    font_back=pg.font.Font("assets/font/GenEiGothicN-SemiBold.otf",30)
    UFO_stop_button=pg.transform.scale(stop_button,(1700//9.2,472//9.2))
    mouse_x=0
    mouse_y=0
    manual_time=0
    
    gemhunterufo_fps=60    
    if on_manual(2):
        UFO_on_manual=True
    else:
        UFO_on_manual=False       
    run=True
    if home_modo[3][0]==True :
        UFO=pg.transform.scale(pg.image.load("assets/UFO/goald//UFO.png"), (int(818//5), int(579//5)))
        itemtype=(pg.transform.scale(pg.image.load("assets/UFO/goald/mushroom.png"), (int(650//8), int(650//8))),
                  pg.transform.scale(pg.image.load("assets/UFO/goald//pine.png"), (int(542//5), int(529//5))),
                  pg.transform.scale(pg.image.load("assets/UFO/goald//tomato.png"),  (int(542//5), int(529//5))),
                  pg.transform.scale(pg.image.load("assets/UFO/goald//muscat.png"), (int(542//5), int(529//5))),
                  pg.transform.scale(pg.image.load("assets/UFO/goald//bread.png"), (int(533//5), int(420//5))),
                  pg.transform.scale(pg.image.load("assets/UFO/goald//beer.png"), (int(682//8), int(682//8))))
        meter=pg.image.load("assets/UFO/goald//meter.png")
    else:
        UFO=pg.transform.scale(pg.image.load("assets/UFO/normal/UFO.png"), (int(818//5), int(579//5)))
        itemtype=(pg.transform.scale(pg.image.load("assets/UFO/normal/mushroom.png"), (int(650//8), int(650//8))),
                  pg.transform.scale(pg.image.load("assets/UFO/normal/strawberryjam.png"), (int(542//5), int(529//5))),
                 pg.transform.scale(pg.image.load("assets/UFO/normal/kiwijam.png"),  (int(542//5), int(529//5))),
                 pg.transform.scale(pg.image.load("assets/UFO/normal/orangejam.png"), (int(542//5), int(529//5))),
                 pg.transform.scale(pg.image.load("assets/UFO/normal/bread.png"), (int(533//5), int(420//5))),
                 pg.transform.scale(pg.image.load("assets/UFO/normal/beer.png"), (int(682//8), int(682//8))))
        meter=pg.image.load("assets/UFO/normal/meter.png")

    while run:
        if meter_y<675:
               meter_y=((pg.time.get_ticks()-timeplus)/40)+30
    #meetaa_Y=675
    #背景 
        screen.fill((14,0,79))
        pg.draw.rect(screen,(93,93,93), (1100,0,200,720))
        pg.draw.rect(screen,(255,169,49), (1100,meter_y,200,720))
        screen.blit(meter,(0,0))
        if UFO_on_manual:
            screen.blit(UFO_stop_button,(1100,5))

        for event in pg.event.get():
            mouse_x,mouse_y=pg.mouse.get_pos()
            if (event.type == pg.KEYDOWN and event.key == pg.K_r) or (event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and meter_y==2000):
                global home_scene
                home_scene=0
                run=False
            if event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 1100 <= mouse_x and mouse_y <= 52:
                manual_time=pg.time.get_ticks()
                manual()
                timeplus+=pg.time.get_ticks()-manual_time
                for i in range(len(item)):
                    item[i][3]+=pg.time.get_ticks()-manual_time
        pressed_key =pg.key.get_pressed()

        UFO_pushedkeycount=0
        for i in range(4):
            if pressed_key[pushedkey[i]]:
                pushedkeycount+=1 

        if UFO_pushedkeycount==2:
            speed=5
        else:
            speed=7
    
        if meter_y>=675:
            speed=0

        if meter_y>=675:
            if UFO_x>640:
                UFO_x-=5
            if UFO_x<640:
                UFO_x+=5
            if UFO_y>350:
                UFO_y-=5
            if UFO_y<350:
                UFO_y+=5
            screen.blit(font_back.render("Rキー：戻る", True, (255,255,255)),(100,30))
            if size<110:
                size+=1
                if home_modo[3][0]==True:
                    UFO=pg.transform.scale(pg.image.load("assets/UFO/goald/UFO.png"), (int(163-163*size//110), int(115-115*size//110))) 
                else:
                    UFO=pg.transform.scale(pg.image.load("assets/UFO/normal/UFO.png"), (int(163-163*size//110), int(115-115*size//110)))             
            if size==110:
                se_last.play()
                size=111
            if meter_y>=675 and not meter_y==2000:
                meter_y=2000
                home_clearcount[3]+=1
                star[3][0][0]=1
                if home_clearcount[3]==1 or home_bestscore[3]<gemcount:
                    home_bestscore[3]=gemcount
                if home_clearcount[3]>=5:
                    star[3][1][0]=1
                    if home_clearcount[3]>=7:
                            star[3][2][0]=1
                            star[3][len(star[3])-1][2]=star_hint[3]
                if fuel_count>=3:
                    star[3][3][0]=1
                if gemcount>=30:
                    star[3][4][0]=1
                    if gemcount>=40:
                        star[3][5][0]=1
        
        if pressed_key[pushedkey[-1-direction]] and  UFO_y>0:
                UFO_y-=speed

        if pressed_key[pushedkey[1-direction]] and UFO_y<limit_y:
                UFO_y+=speed

        if pressed_key[pushedkey[-direction]] and  UFO_x<limit_x:
                UFO_x+=speed

        if pressed_key[pushedkey[-2-direction]] and  UFO_x>0:
                UFO_x-=speed

        for i in range(len(item)):
                if item[i][2]==1 and (item[i][3]+5000)<pg.time.get_ticks() and meter_y<=675:
                    item[i]=[random.randrange(900),random.randrange(600),0,pg.time.get_ticks()-1500+(random.randrange(30)*100),random.randrange(1000)]
                if item[i][2] ==0:
                     if (item[i][3]+10000)<pg.time.get_ticks() or meter_y>=675:
                        item[i][2]=1
                        item[i][3]=pg.time.get_ticks()-1500+(random.randrange(30)*100)
                     if item[i][4]>970:
                        screen.blit(itemtype[4],(item[i][0],item[i][1]))
                     elif item[i][4]>870:
                        screen.blit(itemtype[0],(item[i][0],item[i][1]))
                     elif item[i][4]>800:
                        screen.blit(itemtype[5],(item[i][0],item[i][1]))
                     elif item[i][4]>532:
                        screen.blit(itemtype[3],(item[i][0],item[i][1]))
                     elif item[i][4]>266:
                        screen.blit(itemtype[2],(item[i][0],item[i][1]))
                     else:
                         screen.blit(itemtype[1],(item[i][0],item[i][1]))
        for i in range(len(item)):
            if item[i][2] ==0 and meter_y<=675:
                if item[i][4]>970:
                    if abs(25+UFO_x-item[i][0])<100 and abs(15+UFO_y-item[i][1])<70:
                        item[i][2]=1
                        item[i][3]=pg.time.get_ticks()-1500+(random.randrange(30)*100)
                        timeplus+=2000
                        fuel_count+=1
                        se_fuel.play()
                elif item[i][4]>870:
                    if abs(40+UFO_x-item[i][0])<100 and abs(17+UFO_y-item[i][1])<77 and (item[i][4]+1500)<pg.time.get_ticks():
                        item[i][2]=1
                        item[i][3]=pg.time.get_ticks()-1500+(random.randrange(30)*100)
                        direction=random.randrange(3)
                        timeplus-=500
                        se_change.play()
                elif item[i][4]>800:
                    if abs(40+UFO_x-item[i][0])<100 and abs(17+UFO_y-item[i][1])<77 and (item[i][4]+1500)<pg.time.get_ticks():
                        item[i][2]=1
                        item[i][3]=pg.time.get_ticks()-1500+(random.randrange(30)*100)
                        direction=random.randrange(3)
                        gemcount+=3
                        se_jem.play()
                else:
                    if abs(25+UFO_x-item[i][0])<90 and abs(UFO_y-item[i][1]-3)<70:
                        item[i][2]=1
                        item[i][3]=pg.time.get_ticks()-1500+(random.randrange(30)*100)
                        gemcount+=1
                        se_jem.play()
        screen.blit(pg.font.Font(home_font,50).render(str(gemcount), True, (255,255,255)),(20,20))
        if meter_y<=675:
            screen.blit(arrow[direction],(1000,0))
        screen.blit(UFO,(UFO_x,UFO_y))

        pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))
        pg.display.update()
        home_clock.tick(gemhunterufo_fps) 
def getstarcount(game):
    getstarcount=len(star[game])-1
    for i in range(len(star[game])-1):
        getstarcount-=star[game][i][0]
    return getstarcount
def manual():
    manual_run=True
    screen.blit(home_manual[home_scene-4],(0,0))
    pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))
    pg.display.update()
    home_se_decision.play()
    while manual_run:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN or (event.type == pg.KEYDOWN and event.key == pg.K_r):
                manual_run=False
    home_se_back.play()
def on_manual(n):
    flag=False
    if (home_clearcount[n]==0 and manual_mode==1) or manual_mode==2:
        flag=True
    return flag
def play_bgm():
    pg.mixer.music.load("assets/home/sound/bgm.wav")
    pg.mixer.music.play(loops=-1)
play_bgm()
#メインループ＝＝＝ ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
while home_run:
    if home_scene==0 or home_scene==1:
        screen.fill((163,38,0))
        screen.blit(home_package[home_y],(0,100))
        pg.draw.rect(screen,(50,50,50), (750,400,600,200)) 
        if home_modo[home_y][0]==True:
                pg.draw.rect(screen,(255,205,43), (750,400,600,200))
        screen.blit(home_screen,(0,0))
        screen.blit(pg.font.Font(home_font,50).render(home_modo[home_y][1], True, (255,255,255)),(900,430))
        screen.blit(pg.font.Font(home_font,21).render("開放条件:"+star_game_name[home_y]+"のスターを全て獲得する", True, (0,0,0)),(718,513))
        screen.blit(pg.font.Font(home_font,40).render(str(home_clearcount[home_y])+"回", True, (0,0,0)),(1000,100))
        screen.blit(pg.font.Font(home_font,40).render(str(home_bestscore[home_y])+home_unit[home_y], True, (0,0,0)),(950,230))
        screen.blit(home_frame[home_x],(0,0))

    if home_scene == 1:
        screen.blit(home_manual[home_y],(0,0))
#星
    if home_scene==2:
         
        screen.fill(white)
        screen.blit(star_background,(0,0))

        pg.draw.rect(screen,(255,202,10), (0,415-star_clearrate,630,355))#60 410
        pg.draw.rect(screen,(255,169,49), (650,115+75*star_y,630,75))
        for i in range (len(star[star_x])):
            screen.blit(font_home_star.render(str(star[star_x][i][1]), True, (0,0,0)),(750,75*i+130))
            if   i<len(star[star_x])-1:
                if  star[star_x][i][0]==1:
                    screen.blit(star_cleared,(675,75*i+125)) 
                else:
                    screen.blit(star_notcleared,(675,75*i+125)) 
            else:
                screen.blit(star_light,(675,75*i+125)) 
        screen.blit(star_screen,(0,0))
        screen.blit(font_home_star_game_name.render(star_game_name[star_x], True, (0,0,0)),(942-(fontsize_home_star_game_name*(len(star_game_name[star_x])-1)/2),30))
        for i in range(len(star[star_x][star_y][2])//13+1):
            screen.blit(font_home_star_game_name.render(star[star_x][star_y][2][13*i:13*i+13:], True, (0,0,0)),(15,500+(fontsize_home_star_game_name*i)))
        pressed_key =pg.key.get_pressed()
#消去
    if home_scene==3:
        screen.blit(home_delete,(0,0))
        if home_x==3:
            screen.blit(home_delete_choice,(750,335))
        else:
            screen.blit(home_delete_choice,(233,335))
#ボタン
    for event in pg.event.get():
            home_click=False
            home_mouse_x,home_mouse_y=pg.mouse.get_pos()
            # if event.type == MOUSEBUTTONDOWN and event.button==1:
                # print( home_mouse_x,home_mouse_y)
            if event.type == pg.QUIT:
                    home_run= False
            if (event.type==pg.KEYDOWN and event.key==pg.K_c) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 936<=home_mouse_x  and 307<=home_mouse_y<=403) :
                if home_scene==0:
                    home_scene=1
                    home_se_decision.play()
                elif home_scene==1:
                    home_scene=0
                    home_click=True
                    home_se_back.play()
            elif  home_scene==1 and event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3):
                home_scene=0
                home_click=True
                home_se_back.play()
            if not home_scene==0 :
                if (event.type==pg.KEYDOWN and event.key==pg.K_r) or (home_scene==2 and  event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and home_mouse_x<=150  and home_mouse_y<=150):
                    home_se_back.play()
                    if not home_scene==1:
                        home_x=0
                        home_click=True
                    if home_scene==3:
                        play_bgm()
                    home_scene=0
            if home_scene==0:
                if event.type==pg.KEYDOWN and event.key==pg.K_RIGHT and home_x<2:
                   home_x+=1
                   home_se_choose.play()
                if event.type==pg.KEYDOWN and event.key==pg.K_LEFT and home_x>0:
                   home_x-=1
                   home_se_choose.play()
                if (event.type==pg.KEYDOWN and event.key==pg.K_UP ) or ( event.type == MOUSEBUTTONDOWN and (((event.button==1 or event.button==3) and 204<=home_mouse_x<=350  and 26<=home_mouse_y<=64) or event.button == 4)) :
                    if home_y==0:
                       home_y=len(star)-1
                    else:
                        home_y-=1
                    home_se_choose.play()
                if (event.type==pg.KEYDOWN and event.key==pg.K_DOWN) or ( event.type == MOUSEBUTTONDOWN and (((event.button==1 or event.button==3) and 204<=home_mouse_x<=350  and 632<=home_mouse_y<=680) or event.button==5)) :
                    if home_y==(len(star)-1):
                       home_y=0
                    else:
                       home_y+=1 
                    home_se_choose.play()
                if (event.type==pg.KEYDOWN and event.key==pg.K_SPACE and home_x==0) or (home_click==False and event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and home_mouse_x<=907  and 100<=home_mouse_y<=574-1.58*(home_mouse_x-600) and home_mouse_y<=570):
                    home_scene=home_y+4
                    pg.mixer.music.stop()
                if (event.type==pg.KEYDOWN and event.key==pg.K_SPACE and home_x==1) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 560<=home_mouse_x<-9/13*(home_mouse_y-560)+1060  and 580<=home_mouse_y):
                    home_scene=2
                    home_se_decision.play()
                    star_clearcount=0
                    for i in range(len(star)):
                        for a in range(len(star[i])):
                            star_clearcount+=star[i][a][0]
                    star_clearrate=355*star_clearcount//star_count
                if (event.type==pg.KEYDOWN and event.key==pg.K_SPACE and home_x==2) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and -9/13*(home_mouse_y-560)+1060<=home_mouse_x  and 580<=home_mouse_y):
                    home_scene=3
                    pg.mixer.music.load("assets/delete/se.mp3")
                    pg.mixer.music.play()
                    break
                if (event.type==pg.KEYDOWN and event.key==pg.K_b ) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 870<=home_mouse_x  and 403<home_mouse_y<=500):
                        if getstarcount(home_y)==0:
                            if home_modo[home_y][0]==False:
                                home_modo[home_y][0]=True
                                home_se_decision.play()
                            else:
                                home_modo[home_y][0]=False
                                home_se_back.play()
                        else:
                            home_se_mistake.play()          
#星
            if home_scene==2 :
                if (event.type==pg.KEYDOWN and event.key==pg.K_RIGHT) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 1212<=home_mouse_x  and home_mouse_y<=105):
                    if  star_x<len(star)-1:
                        star_x+=1
                        star_y=0
                    else:
                        star_x=0
                        star_y=0
                    str_se_choice.play()
                elif (event.type==pg.KEYDOWN and event.key==pg.K_LEFT) or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 650<=home_mouse_x<=720  and home_mouse_y<=105):
                    if star_x>0:
                        star_x-=1
                        star_y=0
                    else:
                        star_x=len(star)-1
                        star_y=0
                    str_se_choice.play()
                elif event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3) and 650<=home_mouse_x  and home_mouse_y>=115:
                    if(home_mouse_y-115)//75<len(star[star_x]):
                        star_y=(home_mouse_y-115)//75
                if event.type==pg.KEYDOWN and event.key==pg.K_UP and star_y>0:
                         star_y-=1
                         home_se_choose.play()
                if event.type==pg.KEYDOWN and event.key==pg.K_DOWN and star_y<len(star[star_x])-1:
                         star_y+=1
                         home_se_choose.play()
#消去 
            if home_scene==3 : 
                if event.type==pg.KEYDOWN and event.key==pg.K_RIGHT:
                    home_x=3
                if event.type==pg.KEYDOWN and event.key==pg.K_LEFT:
                    home_x=2
                if (event.type==pg.KEYDOWN and event.key==pg.K_SPACE )or ( event.type == MOUSEBUTTONDOWN and (event.button==1 or event.button==3)):
                    if home_x==3 or ( 790<=home_mouse_x<=1000  and 360<home_mouse_y<=470):
                        home_modo=[[False,"???"] for i in range(len(home_unit))]
                        home_bestscore=["-" for i in range(len(home_modo))]
                        home_clearcount=[0 for i in range(4)]
                        star=copy.deepcopy(star_liset)
                        home_scene=0
                        home_x=0
                        play_bgm()
                    elif  event.type==pg.KEYDOWN or ( 230<=home_mouse_x<=525  and 326<home_mouse_y<=500):
                        home_se_back.play()
                        home_scene=0
                        home_X=0
                        play_bgm()
                if event.type==pg.KEYDOWN and home_mouse_x<10 and home_mouse_y<10 and home_x==3 and home_y==2:#サーモンに合わせて消去　消去するにカーソルを合わせる　マウスを右上　
                    if event.key==pg.K_0:
                        manual_mode=0
                    if event.key==pg.K_1:
                        manual_mode=1
                    if event.key==pg.K_2:
                        manual_mode=2
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    home_run=False

            event=None
            pg.event.clear
    if home_scene>=4:
        if home_scene==4:
            fish()
            if getstarcount(0)==0:
                home_modo[0][1]="ラノベモード"
        if home_scene==5:
            window()
            if getstarcount(1)==0 :
                home_modo[1][1]="チョコモード"
        if home_scene==6:
            salmon()
            if getstarcount(2)==0:
                home_modo[2][1]="炙りモード"
        if home_scene==7:
            UFO()
            if getstarcount(3)==0:
               home_modo[3][1]="ゴールドモード"
        play_bgm() 
#更新
    pg.draw.rect(screen, (0, 0, 0), (0, screen_height, screen_width, black_line_y))
    pg.display.update()
    home_clock.tick(home_fps)
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
pg.quit()