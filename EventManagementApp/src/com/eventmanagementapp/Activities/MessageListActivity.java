package com.eventmanagementapp.Activities;

import java.util.ArrayList;

import android.app.ActionBar;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;

import com.eventmanagementapp.R;
import com.eventmanagementapp.adapter.MessagesListAdapter;

public class MessageListActivity extends FragmentActivity{

	ListView lvMessages;
	ArrayList<String> listMessages;
	MessagesListAdapter adapterMessageList;
	Button btnBack;
	Context mContext;
	
	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		setContentView(R.layout.messagetab);
		mContext=MessageListActivity.this;
		ActionBar actionBar = getActionBar();
		actionBar.setDisplayShowHomeEnabled(false);
		actionBar.setDisplayShowTitleEnabled(false);
		LayoutInflater mInflater = LayoutInflater.from(this);
		View mCustomView = mInflater.inflate(R.layout.customactionbarview, null);
		actionBar.setCustomView(mCustomView);
		btnBack=(Button) mCustomView.findViewById(R.id.btnBack);
		actionBar.setDisplayShowCustomEnabled(true);

		lvMessages=(ListView)findViewById(R.id.lvMessages);
		listMessages=new ArrayList<String>();
		listMessages.add("Andy Lau");
		listMessages.add("James Moore");
		listMessages.add("Jorgen Flood");
		listMessages.add("Claude");
		listMessages.add("Stefanos Fanidis");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		adapterMessageList=new MessagesListAdapter(mContext, listMessages);
		lvMessages.setAdapter(adapterMessageList);
		lvMessages.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent=new Intent(mContext,MessageChatActivity.class);
				startActivity(myIntent);
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
		btnBack.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				finish();	
				overridePendingTransition(R.anim.right_in, R.anim.right_out);				
			}
		});
	}
	
	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
