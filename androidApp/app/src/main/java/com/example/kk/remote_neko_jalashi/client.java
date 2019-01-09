package com.example.kk.remote_neko_jalashi;

import android.util.Log;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class client {

    private int onX,onY;

    public client(int x,int y){
        this.onX = x;
        this.onY = y;
    }

    //ラズパイとTCP通信で座標情報を送信
    public void sendTouchInfo(String server,int port){
        try {
            //String server = "192.168.43.135";
            //int port = 8000; //サーバー側のポート番号
            Socket s = new Socket(server, port);

            // サーバーに数値を送信
            OutputStream os = s.getOutputStream();
            DataOutputStream dos = new DataOutputStream(os);
            dos.writeInt(onX);

            // 演算結果を受信
            InputStream is = s.getInputStream();
            DataInputStream dis = new DataInputStream(is);
            int res = dis.readInt();
            System.out.println(res);
            Log.d("Server",String.valueOf(res));

            // ストリームを閉じる
            dis.close();
            dos.close();
        }
        catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }

    public void setOnX(int onX) {
        this.onX = onX;
    }

    public void setOnY(int onY) {
        this.onY = onY;
    }

}
