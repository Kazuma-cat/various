score ="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">























<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Language" content="ja" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta name="format-detection" content="telephone=no"/>
    <title>
    
    
      NAGOYA UNIVERSITY
    
    </title>


    <script>
      var waitingMessage = "お待ちください...";
      var showBlockAlartMessage = "処理中です。しばらくお待ちください。";
      var sessionExpirationAlertMessage = "まもなくセッションタイムアウトします。下のボタンからセッションタイムアウトを回避できます。";
      var sessionContinuationButton = "セッションを継続する";
      var sessionExpirationNotifyMessage = "セッションタイムアウトした恐れがあります。画面上の設定、若しくは入力内容があればお手元に控えた上で、再度ログインしてください。";
      var closeAlertDialog = "閉じる";
      var ajaxRequestError = "エラーが発生しました";
      var addListenerError = "お使いのブラウザは対応していません。";
      var noFoundResourceError = "存在しないファイルが指定されています。指定し直して下さい。";
    </script>

    <link rel="stylesheet" href="./css/timepicker.css" type="text/css" charset="utf-8"/>
    <link rel="stylesheet" href="./css/jquery.ui.css" type="text/css" charset="utf-8" /> 
    <link rel="stylesheet" href="./css/design02/common.css" type="text/css" media="screen" charset="utf-8" />
    <link rel="stylesheet" href="./css/design02/theme.css" type="text/css" media="screen" charset="utf-8" />
    <!--<link rel="stylesheet" href="./css/design02/common_en.css" type="text/css" media="screen" charset="utf-8" />-->
    <!--<link rel="stylesheet" href="./css/design02/theme_en.css" type="text/css" media="screen" charset="utf-8" />-->
    <link rel="stylesheet" href="./css/design02/common_print.css" type="text/css" media="print" charset="utf-8" />
    <link rel="stylesheet" href="./css/design02/theme_print.css" type="text/css" media="print" charset="utf-8" />
    <!--<link rel="stylesheet" href="./css/design02/theme_print_en.css" type="text/css" media="print" charset="utf-8" />-->
    <link rel="shortcut icon" href="./img/design02/favicon.ico" />

    <script language="JavaScript" type="text/JavaScript" src="./js/prototype.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/effects.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/main.js"></script>
<!--[if IE]>
    
    <script language="JavaScript" type="text/JavaScript" src="./js/excanvas.js"></script>
<![endif]-->

    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.js"></script>
    <script type="text/javascript">jQuery.noConflict();var jq$ = jQuery;</script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.ui.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/date.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/design02/common.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/design02/theme.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.ui.datepicker-ja.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.timePicker.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.numeric.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.blockUI.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/jquery.mousewheel.js"></script>
    <script language="JavaScript" type="text/JavaScript" src="./js/main_jq.js"></script>
    <script language="javascript" type="text/javascript">
    <!--
      restoreScreenState('', '', '');
      
      
      if (false) {
          monitoringSessionExpiration = startSessionExpirationMonitoring(3600, 300, 10);
          monitoringSessionExpiration.initializeTimer();
          window.addEventListener('resize', function(eve){
              var resizeTimer = false;
              if (resizeTimer !== false) {
                  clearTimeout(resizeTimer);
              }
              resizeTimer = setTimeout(function() {
                  monitoringSessionExpiration.resetPositioning();
              }, 50);
          }, false);
      }
    //-->
    </script>

  </head>

<body>
<div id="container">
<div id="header">
  
  
  <div id="head_top"></div>
  <div id="head_left"></div>
  <div id="head_right">
    <div class="button">
      
      <input name="f_large" type="button" id="f_large" />
      <input name="f_middle" type="button" id="f_middle" />
      <input name="f_small" type="button" id="f_small" />
      
      
        <span id="help_space" > </span>
        
        
        
        
          <form name="logoutForm" method="post" action="/camweb/logout.do">
            <input name="logout" type="button" id="logout" onclick="return logoutCheck('ログアウトしますか？');" />
          </form>
        
      
    </div>
  </div>
  <div class="clear"></div>
  <div id="head_base"></div>
  
  <div id="top_menu">
    <ul id="nav">

      
        
















  
    <li ><a href="tab.do?buttonName=changeTab&menulv1=0000000001" ><span class="bkimg">HOME</span></a>
      <ul id="menu_list">
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="メッセージ受信一覧" href="
                top.do?buttonName=showContent&menulv1=0000000001&menuIndex=0&contenam=wbasmgjr&kjnmnNo=3
                ">メッセージ受信一覧
              </a>
            
          </li>
        
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="ブックマーク登録" href="
                top.do?buttonName=showContent&menulv1=0000000001&menuIndex=1&contenam=wbasbkmu&kjnmnNo=7
                ">ブックマーク登録
              </a>
            
          </li>
        
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="メッセージ転送設定" href="
                top.do?buttonName=showContent&menulv1=0000000001&menuIndex=2&contenam=wbasmfwu&kjnmnNo=8
                ">メッセージ転送設定
              </a>
            
          </li>
        
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="キャビネット一覧" href="
                top.do?buttonName=showContent&menulv1=0000000001&menuIndex=3&contenam=prtlcabu&kjnmnNo=9
                ">キャビネット一覧
              </a>
            
          </li>
        
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="個人種別選択" href="
                top.do?buttonName=showContent&menulv1=0000000001&menuIndex=4&contenam=wbaskjsu&kjnmnNo=11
                ">個人種別選択
              </a>
            
          </li>
        
      
      </ul>
    </li>
  
    <li ><a href="tab.do?buttonName=changeTab&menulv1=0000000002" ><span class="bkimg">教務掲示</span></a>
      <ul id="menu_list">
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="教務掲示一覧" href="
                top.do?buttonName=showContent&menulv1=0000000002&menuIndex=0&contenam=prtlkkir&kjnmnNo=16
                ">教務掲示一覧
              </a>
            
          </li>
        
      
      </ul>
    </li>
  
    <li ><a href="tab.do?buttonName=changeTab&menulv1=0000000003" ><span class="bkimg">履修・成績</span></a>
      <ul id="menu_list">
      
        
        

        
        
          <li>
            
            
              <a style = "padding-left:15px;padding-right:15px" title="修得科目確認（成績照会）" href="
                wssrlstr.do?clearAccessData=true&contenam=wssrlstr&kjnmnNo=29
                ">修得科目確認（成績照会）
              </a>
            

            
            
          </li>
        
      
      </ul>
    </li>
  
    <li class='menu_end'><a href="tab.do?buttonName=changeTab&menulv1=0000000004" ><span class="bkimg">シラバス</span></a>
      <ul id="menu_list">
      
        
        

        
        
          <li>
            
            

            
            
              <a style = "padding-left:15px;padding-right:15px" title="シラバス検索" href="
                top.do?buttonName=showContent&menulv1=0000000004&menuIndex=0&contenam=slbssrch&kjnmnNo=98
                ">シラバス検索
              </a>
            
          </li>
        
      
      </ul>
    </li>
  

      
      

    </ul>
    <br class="clear" />
  </div>
</div>

<div id="content">
  <table cellpadding="0" cellspacing="0" summary="layout">
    <tr>
      
      










<div id="login_inf_print">
  <div class="top"></div>
  <div class="mid">
    
    <ul class="user">
      <li class="label">ログインユーザ ：</li>
      <li class="item"> </li>
      <li class="item">植村　和真</li>
    </ul>
  
  </div>
  <div class="under"></div>
</div>


      
      







<td id="main">
  
    
    <div id="title">
      <h2>
        修得科目確認（成績照会）
      </h2>
    </div>
    
  


























  



<form name="kyomuActionForm" method="post" action="/camweb/wssrlstr.do">
<input type="hidden" name="buttonName" value=""/>
<input type="hidden" name="timestamp" value="1604931991617"/>


  <div class="caption" style="line-height:2em">





    
    
      
        <span class="image"></span><span class="h4 line4">科目ごとの成績を確認してください。</span>
        <br>
      
    
</div>

  
  <p id="listTop"></p>

  
  <div class="contents_1">
    <div class="function_bottom" style="margin-bottom: 10px;">
      
     	 <h4 class="do_not_print" style="text-align:left;margin-left: 20px;">[成績公開日時：2020/10/19 09:00]</h4>
      
      <h4 class="do_not_print" style="text-align:right;margin-right: 20px;">プレビューで確認して下さい</h4><br>
      <input style="float:right;margin-right: 20px;" type="button" onclick="return window.print();" value="印刷する" class="run decorate"/>
    </div>
  </div>

  <div class="contents_1">
    <div id="tabnavigation_list">
      <ul>
        
        
          
            <li class="active" style="border-right:none;width:140px;height:34px;line-height:34px;">科目一覧を見る</li>
          
          
        
        
        
          
            <li style="border-right:none;width:140px;height:34px;line-height:34px;"><A id="goTani" href="#" onclick="return exec('showCreditAcquirement',this,null)">単位修得状況を見る</A></li>
          
          
          
        
        
        
          <li style="width:140px;height:34px;line-height:34px;"><A id="goGpa" href="#" onclick="return exec('showGpaResult',this,null)">GPAを見る</A></li>
        
      </ul>
    </div>
    <br>

    <table class="list" style="margin-top:0px;margin-left:20px;border:1px solid #777777;">
      <tr class="label">
        <td style="white-space:nowrap" width="50%" align="center">分野系列名／科目名</td>
        <td style="white-space:nowrap" align="center">単位</td>
        
        
          <td style="white-space:nowrap" align="center">評価</td>
        
        <td style="white-space:nowrap" align="center">年度</td>
        <td style="white-space:nowrap" align="center">期間</td>
        <td style="white-space:nowrap" align="center">成績担当教員</td>
      </tr>

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>基礎セミナー</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  基礎セミナーＡ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">西山　久雄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  基礎セミナーＢ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">日比　嘉高</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>言語文化</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  英語（基礎）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｃ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">加藤　高志</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  英語（中級）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">WATSON Alex</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  英語（コミュニケーション）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">WEEKS Mark</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  英語（上級）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">村尾　玲美</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  ロシア語１
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">柳沢　民雄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  ロシア語２
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">タチアナ　ヤマザキ</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  ロシア語３
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">柳沢　民雄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  ロシア語４
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">SAVELIEV IGOR</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>健康・スポーツ科学（講義）</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  健康・スポーツ科学講義
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">山本　裕二</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>健康・スポーツ科学（実習）</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  健康・スポーツ科学実習Ⅰ（フィットネス）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">水野　貴正</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  健康・スポーツ科学実習Ⅱ（太極拳）
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">張　成忠</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>文系基礎科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  心理学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">清河　幸子</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  日本国憲法
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">河北　洋介</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>文系教養科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  産業社会と企業
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">中屋　信彦</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>理系基礎科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学基礎Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">髙木　秀夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学基礎Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">村上　慧</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">槇　亙介</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1.5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">深澤　愛子</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物学基礎Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">五島　剛太</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物学基礎Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">本間　道夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  線形代数学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">谷川　好男</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  線形代数学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">谷川　好男</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  地球科学基礎Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">西村　浩一</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  地球科学基礎Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">竹内　誠</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  電磁気学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">小林　義明</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  微分積分学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">内藤　久資</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  微分積分学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">内藤　久資</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理学基礎Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">戸本　誠</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>理系教養科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  情報科学入門
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">間瀬　健二</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物質世界の認識
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">樫田　啓</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>専門基礎科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学講究Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">阿部　洋</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学講究Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">阿部　洋</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  計算化学概論
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">柳井　毅</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理化学基礎
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">菱川　明栄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  分析化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">田中　健太郎</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  分析化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">田中　健太郎</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">唯　美津木</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">唯　美津木</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学Ⅲ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">大木　靖弘</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学Ⅳ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">松本　剛</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    4
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">山口　茂弘</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">伊丹　健一郎</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機化学Ⅲ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">伊藤　英人</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理化学
                </td>
                <td style="text-align:center">&nbsp;
                  
                    4
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">阿波賀　邦夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  量子化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    4
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">柳井　毅</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  量子化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">菱川　明栄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">阿部　洋</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">阿部　洋</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>専門科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  分析化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    3
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">田中　健太郎</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    4
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">荘司　長三</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    3
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">村上　慧</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">阿部　洋</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理化学実験
                </td>
                <td style="text-align:center">&nbsp;
                  
                    5
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">松下　未知雄</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学演習Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2020</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">柳井　毅</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学演習Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2020</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">柳井　毅</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機化学特論
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">髙木　秀夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機化学特論Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">斎藤　進</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  有機機器分析
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">村上　慧</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物化学特論
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                        
                          <span style="color:red">欠席</span>
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">猪子　誠人</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  化学統計力学
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">青柳　忍</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物性化学Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">阿波賀　邦夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物性化学Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">阿波賀　邦夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  無機物化機器分析
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2019</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">田中　健太郎</td>
              </tr>
            
          
        

      

        
          <tr class="column_even">
          
          
            <td colspan="6" style="">
              <strong>教職科目・随意科目</strong>
            </td>
          </tr>
        

        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生物学基礎Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                        
                          <span style="color:red">欠席</span>
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">吉岡　泰</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  数学展望Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">伊師　英之</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  数学演習Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;春</td>
                <td style="text-align:center">大久保　俊</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  数学演習Ⅱ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">久本　智之</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  物理学基礎演習Ⅰ
                </td>
                <td style="text-align:center">&nbsp;
                  
                    1
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">田村　陽一</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  生化学１
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ｂ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2018</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">YOU Young-Jai</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  教職基礎論
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                          Ａ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">三羽　光彦</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  教育原理
                </td>
                <td style="text-align:center">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center">&nbsp;
                    
                      
                        
                        
                          <span style="color:red">欠席</span>
                        
                      
                    
                  </td>
                
                <td style="text-align:center">2017</td>
                <td style="text-align:center">&nbsp;秋</td>
                <td style="text-align:center">三宅　正夫</td>
              </tr>
            
          
        

      

        

        
          
          
            
            
              <tr class="column_odd">
              
              
                <td style="background-image:none">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  教育方法論
                </td>
                <td style="text-align:center;background-image:none">&nbsp;
                  
                    2
                  
                </td>
                
                
                  <td style="text-align:center;background-image:none">&nbsp;
                    
                      
                        
                          Ｓ
                        
                        
                      
                    
                  </td>
                
                <td style="text-align:center;background-image:none">2017</td>
                <td style="text-align:center;background-image:none">&nbsp;秋</td>
                <td style="text-align:center;background-image:none">谷　伊織</td>
              </tr>
            
          
        

      
    </table>
  </div>
  <div align="right" style="margin-right: 20px;"><a href="#listTop">▲ページ上部へ移動する</a></div>
</form>
</td>
      
      
















<td id="sub1">
  <div id="navigation">
   
    
    <div id="login_inf">
      <div class="top"></div>
      <div class="mid">
      
        <ul class="date">
          <li class="label"></li>
          <li class="item">
            
            2020年11月7日
            
          </li>
          <li class="item">
            
            17時1分
            
          </li>
        </ul>
        <ul class="user">
          <li class="label"></li>
        
          <li class="item">植村　和真</li>
        
        </ul>
        <form name="genericForm" method="post" action="/camweb/changeLocale999.do">
          <input type="hidden" name="buttonName" value="">
          <input type="hidden" name="lang" value="2">
          <div style="width:90%;text-align:center;padding-top:5px;">
            <input class="decorate" onclick="return exec('changeLocale',this)" type="button" value="Change English">
          </div>
        </form>
      </div>
      <div class="under"></div>
    </div>
   
   

  
  
    
    <br/>
    
    <div id="side_menu">
      <div class="top"></div>
        <div id="slide">
          <input type="button" class="button" />
        </div>
      <div class="mid" id="sideMenuMiddle">
        
          
            
          











  <ul>
    <li class="label">履修登録</li>
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]★★最初に必ず読んでください★★</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]**Be sure to read this first**</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録（英語科目）</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録（情報リテラシー(文系)）</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録（特別履修科目）</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録状況確認</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修確認</a>
        </li>
      
      
      
    
      
      
        <li class="item">
          <a href="#" style="cursor:default">[使用期間外]履修登録エラーリスト</a>
        </li>
      
      
      
    
  </ul>

        
          
            
          











  <ul>
    <li class="label">修得科目確認（成績確認）</li>
    
      
      
      
      
        
        
        
        
            <li class="item">
              <a title="修得科目確認（成績照会）" href="
                wssrlstr.do?clearAccessData=true&contenam=wssrlstr&kjnmnNo=29
                ">修得科目確認（成績照会）
              </a>
            </li>
        
      
    
  </ul>

        
        
        
      </div>
      <div class="under"></div>
    </div>
  
  </div>
  <div id="dummy"></div>
  <br class="clear" />
</td>

    </tr>
  </table>
</div>

<p id="pageTopButton">
  <a href="#wrap" id="pageTopLink">PAGE TOP</a>
</p>





<script type="text/javascript">

jQuery(function(){
  target = document.getElementById("copyright");
  
});

</script>

  <noscript><c:out value="JavaScriptを使用できる環境でご利用ください。" /></noscript>
  <div id="footer">
    <div class="text" id="copyright"/>
  </div>

</div>
</body>
</html>
"""
