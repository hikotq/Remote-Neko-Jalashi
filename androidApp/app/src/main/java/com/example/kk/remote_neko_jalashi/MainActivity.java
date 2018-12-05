package com.example.kk.remote_neko_jalashi;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.webkit.WebView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        WebView webView1 = findViewById(R.id.webView1);
        webView1.getSettings().setJavaScriptEnabled(true);
        webView1.loadUrl("http://192.168.43.13:8080/stream_simple.html"); //HTMLファイルを配置したURL
    }
    /*
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    */

}