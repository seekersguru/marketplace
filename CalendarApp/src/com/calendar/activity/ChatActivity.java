package com.calendar.activity;

import java.util.ArrayList;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import com.calendar.adapter.ChatAdapter;
import com.calendarapp.R;
import com.loopj.android.image.SmartImageView;

public class ChatActivity extends FragmentActivity{

	Button btnBack,btnSendMessage;
	ListView lvChat;
	ChatAdapter adapter;
	ArrayList<String> listChat;
	EditText etMessage;
	SmartImageView imViewContact;

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.chatactivity);
		imViewContact=(SmartImageView) findViewById(R.id.imViewContact);
		etMessage=(EditText) findViewById(R.id.etMessage);
		btnSendMessage=(Button) findViewById(R.id.btnSendMessage);
		btnBack=(Button) findViewById(R.id.btnBack);
		lvChat=(ListView) findViewById(R.id.lvChat);
		listChat=new ArrayList<String>();
		listChat.add("Hi");
		listChat.add("Hello");
		imViewContact.setImageResource(R.drawable.no_image);
		adapter=new ChatAdapter(ChatActivity.this, listChat);
		lvChat.setAdapter(adapter);
		btnSendMessage.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				if(!etMessage.getText().toString().trim().equals(""))
				{
					adapter.listChat.add(etMessage.getText().toString());
					adapter.notifyDataSetChanged();
					etMessage.setText("");
				}
			}
		});
		btnBack.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				ChatActivity.this.finish();		
			}
		});
	}
}
