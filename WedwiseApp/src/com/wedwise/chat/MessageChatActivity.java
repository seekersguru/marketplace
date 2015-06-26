package com.wedwise.chat;

import java.util.ArrayList;

import android.content.Context;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import com.wedwise.adapter.ChatAdapter;
import com.wedwiseapp.R;
import com.wedwiseapp.util.CustomFonts;

public class MessageChatActivity extends FragmentActivity{

	Toolbar toolbar;
	Context mContext;
	ImageView imViewOverflowMenuicon,imViewAttachment;
	Button btnBack,btnSendMessage;
	TextView tvToolBar;
	ListView lvChatMessages;
	ChatAdapter adapterChat;
	ArrayList<String> listChat;

	@SuppressWarnings("deprecation")
	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.messagechatactivity);
		mContext=MessageChatActivity.this;
		toolbar=(Toolbar) findViewById(R.id.toolbar);
		toolbar.setBackgroundColor(Color.parseColor("#ffffff"));
		lvChatMessages=(ListView) findViewById(R.id.lvChatMessages);
		btnBack=(Button) toolbar.findViewById(R.id.btnBack);
		btnSendMessage=(Button) findViewById(R.id.btnSendMessage);
		tvToolBar=(TextView)toolbar.findViewById(R.id.tvToolBar);
		imViewOverflowMenuicon=(ImageView)toolbar.findViewById(R.id.imViewOverFlow);
		imViewAttachment=(ImageView) toolbar.findViewById(R.id.imViewAttachment);
		imViewOverflowMenuicon.setBackgroundResource(R.drawable.overflow_menu);
		imViewAttachment.setVisibility(View.VISIBLE);
		imViewOverflowMenuicon.setVisibility(View.VISIBLE);
		tvToolBar.setText("Sujata Weds Rajesh");
		tvToolBar.setTextColor(Color.parseColor("#555555"));
//		CustomFonts.setFontOfTextView(mContext, tvToolBar,"fonts/GothamRnd-Light.otf");
		btnBack.setBackground(MessageChatActivity.this.getResources().getDrawable(R.drawable.back_orange));
		listChat=new ArrayList<String>();
		listChat.add("Time or slot, some unique identifier");
		listChat.add("ok");
		listChat.add("Howz you?");
		listChat.add("I am f9 ,you say?");
		listChat.add("Howz everyone?");
		listChat.add("All are fine here");
		listChat.add("What about vacations?");
		adapterChat=new ChatAdapter(MessageChatActivity.this,listChat);
		lvChatMessages.setAdapter(adapterChat);
		btnBack.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				finish();		
				overridePendingTransition(R.anim.right_in, R.anim.right_out);
			}
		});
		btnSendMessage.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				
			}
		});
	}

	@Override
	public boolean onPrepareOptionsMenu(Menu menu) {
		MenuItem item= menu.findItem(R.id.action_settings);
		item.setVisible(false);
		return true;
	}

	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
