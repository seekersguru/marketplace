package com.wedwise.adapter;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.wedwiseapp.R;

public class MessagesListAdapter extends BaseAdapter{

	Context mContext;
	ArrayList<String> listMessages;

	public MessagesListAdapter(Context mContext,ArrayList<String> listMessages)
	{
		this.mContext=mContext;	
		this.listMessages=listMessages;
	}

	@Override
	public int getCount() {
		// TODO Auto-generated method stub
		return listMessages.size();
	}

	@Override
	public Object getItem(int position) {
		return position;
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		View listItem = convertView;
		LayoutInflater inflater = ((Activity) mContext).getLayoutInflater();
		listItem = inflater.inflate(R.layout.messagelistadapter, parent, false);
		TextView tvContactName=(TextView) listItem.findViewById(R.id.tvContactName);
		TextView tvDate=(TextView) listItem.findViewById(R.id.tvDate);
		TextView tvSubject=(TextView) listItem.findViewById(R.id.tvSubject);
		TextView tvDescription=(TextView) listItem.findViewById(R.id.tvDescription);
		ImageView imViewAtttachment=(ImageView) listItem.findViewById(R.id.imViewAttachment);
		tvContactName.setText(listMessages.get(position));
		return listItem;
	}

}
