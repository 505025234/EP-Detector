from enum import Enum, unique


@unique
class Behaviour(Enum):
    click = 0 #单击
    combieSwipe = 1 
    rightSwipe = 2 #右滑
    leftSwipe = 3 #左滑
    downSwipe = 4 #下滑
    upSwipe = 5 #上滑
    tripleSwipe = 6 #三指滑动
    rightScroll = 7 #右滚动
    leftScroll = 8 #左滚动
    downScroll = 9 #下滚动
    upScroll = 10 #上滚动
    longClick = 11 #长按
    doubleClick = 12 #双击
    doubleSwipe = 13 #二指滑动
    noneBehaviour = 14 #无操作
    misDoubleClick1 = 15 #第一次单击第二次时间稍长
    misDoubleClick2 = 16 #第一次时间稍长，第二次单击
    misLongClick1 = 17 #单击一下再长按
    
    
    misRightSwipe = 18 #右滑mis 单机后右滑
    misLeftSwipe = 19 #左滑mis
    misDownSwipe = 20 #下滑mis
    misUpSwipe = 21 #上滑mis


    misRightScroll1 = 22 #右滚动mis1  单击后拖动
    misLeftScroll1 = 23 #左滚动
    misDownScroll1 = 24 #下滚动
    misUpScroll1 = 25 #上滚动

    misRightScroll2 = 26 #右滚动mis2  拖动后长按
    misLeftScroll2 = 27 #左滚动
    misDownScroll2 = 28 #下滚动
    misUpScroll2 = 29 #上滚动

    misRightScroll3 = 30 #右滚动mis3  拖动后长按拖动
    misLeftScroll3 = 31 #左滚动
    misDownScroll3 = 32 #下滚动
    misUpScroll3 = 33 #上滚动

    misRightScroll4 = 34 #右滚动mis4  滑动后拖动
    misLeftScroll4 = 35 #左滚动
    misDownScroll4 = 36 #下滚动
    misUpScroll4 = 37 #上滚动

    misRightScroll5 = 38 #右滚动mis5  拖动中断又拖动
    misLeftScroll5 = 39 #左滚动
    misDownScroll5 = 40 #下滚动
    misUpScroll5 = 41 #上滚动

    misLongClick2 = 42 #短时间的长按

    sysHome = 43
    sysMenu = 44
    sysExit = 45



@unique
class ErroProType(Enum):
    ProcError = 0
    RamError = 1
    NetError = 2


clickActList = [Behaviour.click,Behaviour.doubleClick]

longClickList = [Behaviour.click,Behaviour.doubleClick,Behaviour.longClick,Behaviour.misLongClick2]

downSwipeActList = [Behaviour.downSwipe,Behaviour.tripleSwipe]

otherSwipeActList = [Behaviour.leftSwipe,Behaviour.leftScroll]


orderBehavList = [Behaviour.click,Behaviour.longClick]