package com.example.kk.remote_neko_jalashi;

import android.app.Activity;
import android.net.Uri;
import android.os.AsyncTask;
import android.util.Log;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class AsyncHttpRequest extends AsyncTask<Uri.Builder, Void, String> {

    private Activity mainActivity;
    String server = MainActivity.ipadd;
    int port = 8000; //サーバー側のポート番号
    Socket s;

    // サーバーに数値を送信
    OutputStream os;
    DataOutputStream dos;

    InputStream is;
    DataInputStream dis;


    public AsyncHttpRequest(Activity activity) {

        // 呼び出し元のアクティビティ
        this.mainActivity = activity;
    }

    // このメソッドは必ずオーバーライドする必要があるよ
    // ここが非同期で処理される部分みたいたぶん。
    @Override
    protected String doInBackground(Uri.Builder... builder) {
        // httpリクエスト投げる処理を書く。
        // ちなみに私はHttpClientを使って書きましたー
        try {

            s = new Socket(server, port);
        // サーバーに数値を送信
        os = s.getOutputStream();
        dos = new DataOutputStream(os);

        is = s.getInputStream();
        dis = new DataInputStream(is);

        while(true) {
                int sendX = ((MainActivity.onX-MainActivity.minX)*450)/(MainActivity.MaxX-MainActivity.minX) + 150;
                int sendY = ((MainActivity.onY-MainActivity.minY)*450)/(MainActivity.MaxY-MainActivity.minY) + 150;

                sendTouchInfo(String.valueOf(sendX)+","+String.valueOf(sendY));
                Thread.sleep(1000);

        }

        } catch (InterruptedException e) {
        e.printStackTrace();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }


    // このメソッドは非同期処理の終わった後に呼び出されます
    @Override
    protected void onPostExecute(String result) {
        // 取得した結果をテキストビューに入れちゃったり
        //TextView tv = (TextView) mainActivity.findViewById(R.id.name);
        //tv.setText(result)
    }

    //ラズパイとTCP通信で座標情報を送信
    public void sendTouchInfo(String PointNum){
        try {
            /*String server = MainActivity.ipadd;
            int port = 8000; //サーバー側のポート番号
            Socket s = new Socket(server, port);

            // サーバーに数値を送信
            OutputStream os = s.getOutputStream();
            DataOutputStream dos = new DataOutputStream(os);
            */
            System.out.println("wait");
            dos = new DataOutputStream(os);
            dos.write(PointNum.getBytes("UTF-8"));
            System.out.println("send");

            // 演算結果を受信
            //InputStream is = s.getInputStream();
            //DataInputStream dis = new DataInputStream(is);
            //int res = dis.readInt();
            //System.out.println(res);
            //Log.d("Server",String.valueOf(res));

            // ストリームを閉じる
            //dis.close();
            //dos.close();
        }
        catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }
}