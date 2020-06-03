package com.example.imageed;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.signature.ObjectKey;

public class Main2Activity extends AppCompatActivity {

    ImageView imageView2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        imageView2=findViewById(R.id.imageView2);
        String link="http://" + getIntent().getStringExtra("ip") + ":5000/showencrypted";
        //imageView2.setImageURI(Uri.parse(getIntent().getStringExtra("ImageUri")));
        Glide.with(this).load(link).signature(new ObjectKey(String.valueOf(System.currentTimeMillis()))).into(imageView2);
    }
}
