package com.example.imageed;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.bumptech.glide.signature.ObjectKey;

import java.io.DataOutput;
import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Main3Activity extends AppCompatActivity {

    ImageView imageView;
    ProgressDialog progressDialog;
    String link=null,link2=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        imageView=findViewById(R.id.imageView);
        link="http://" + getIntent().getStringExtra("ip") + ":5000/decrypt";
        link2="http://" + getIntent().getStringExtra("ip") + ":5000/showdecrypted";
        progressDialog=new ProgressDialog(this);
        progressDialog.setCanceledOnTouchOutside(false);
        progressDialog.setCancelable(false);
        progressDialog.setMessage("Please Wait!");
        progressDialog.show();
        OkHttpClient client1 = new OkHttpClient();
        Request request1 = new Request.Builder()
                .url(link)
                .build();

        client1.newCall(request1).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                // Cancel the post on failure.
                call.cancel();
                Log.d("FAIL", e.getMessage());

                // In order to access the TextView inside the UI thread, the code is executed inside runOnUiThread()
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        final Handler handler = new Handler();
                        handler.postDelayed(new Runnable() {
                            @Override
                            public void run() {
                                // Do something after 5s = 5000ms
                                progressDialog.dismiss();
                                Glide.with(Main3Activity.this).load(link2).signature(new ObjectKey(String.valueOf(System.currentTimeMillis()))).into(imageView);
                            }
                        }, 70000);
                    }
                });
            }

            @Override
            public void onResponse(Call call, final Response response)
            {
                call.cancel();
                Log.d("FAIL","inOn");
                // In order to access the TextView inside the UI thread, the code is executed inside runOnUiThread()
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        final Handler handler = new Handler();
                        handler.postDelayed(new Runnable() {
                            @Override
                            public void run() {
                                // Do something after 5s = 5000ms
                                progressDialog.dismiss();
                                Glide.with(Main3Activity.this).load(link2).signature(new ObjectKey(String.valueOf(System.currentTimeMillis()))).into(imageView);
                            }
                        }, 70000);
                    }
                });
            }
        });
    }
}
