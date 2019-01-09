package com.example.kk.remote_neko_jalashi;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.Menu;
import android.view.MotionEvent;
import android.webkit.WebView;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class MainActivity extends Activity {

    //テスト用のTextView
    private TextView tap;

    //猫じゃらしアイコンのImageView
    private ImageView image_View;
    //猫じゃらしの描画領域
    final static int minX=60,minY=735,MaxX=565,MaxY=910;
    //onTouchの座標
    static int onX=(minX+MaxX)/2,onY=(minY+MaxY)/2;

    //ラズパイ側のカメラ出力用のWebView
    private WebView web_View;
    //ラズパイのIP
    final static String ipadd = "192.168.43.13";

    //クライアントクラス
    //private client client_server = new client(onX,onY);


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //テスト用のタッチ情報表示に使用
        this.tap = findViewById(R.id.textView);

        //猫じゃらしのアイコンをセット
        image_View = this.findViewById(R.id.imageView);

        //image_View.layout(start_xPoint, start_yPoint, start_xPoint+image_View.getWidth(), start_yPoint+image_View.getHeight());

        //ラズパイ側のカメラ出力
        web_View = findViewById(R.id.webView);
        web_View.getSettings().setJavaScriptEnabled(true);
        web_View.loadUrl("http://"+ipadd+":8080/android_output.html"); //HTMLファイルを配置したURL


 /*
        final Handler handler = new Handler();
        final Runnable r = new Runnable() {
            //int count = 0;
            @Override
            public void run() {
                // UIスレッド
               count++;
                if (count > 5) { // 5回実行したら終了
                    return;
                }


                client_server.sendTouchInfo(ipadd,8000);

                //sendTouchInfo(onY);

                handler.postDelayed(this, 1000);
            }
        };
        handler.post(r);
                */
        // httpリクエストを入れる変数
        Uri.Builder builder = new Uri.Builder();

        AsyncHttpRequest task = new AsyncHttpRequest(this);
        task.execute(builder);

    }

    //猫じゃらしアイコンの移動
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        // TODO 自動生成されたメソッド・スタブ

        //タッチしたＸ座標
        int x = (int) event.getRawX();
        //タッチしたＹ座標
        int y = (int) event.getRawY();

        //テスト用
        tap.setText("X座標 "+x+"，Y座標 " + y);

        //x座標の移動
        if(minX<x && x<MaxX) {
            image_View.setX((float) (x - image_View.getWidth() * 2 / 3));
            onX=x;
            //client_server.setOnX(onX);
            //client_server.sendTouchInfo(ipadd,8000);
            //sendTouchInfo(x);
        }else{
        }

        //y座標の移動
        if(minY<y && y<MaxY) {
            image_View.setY((float) (y - image_View.getHeight() * 2 / 3));
            onY=y;
            //client_server.setOnY(onY);
            //sendTouchInfo(y);
        }else{
        }

        //sendTouchInfo(x,y);
        return true;

    }

}