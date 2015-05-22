package com.calendar.adapter;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.calendarapp.R;

public class SubListAdapter extends BaseAdapter{

	Context mContext;
	ArrayList<String> listItems;

	public SubListAdapter(Context mContext,ArrayList<String> listItems)
	{
		this.mContext=mContext;
		this.listItems=new ArrayList<String>();
		this.listItems=listItems;
	}

	@Override
	public int getCount() {
		return listItems.size();
	}

	@Override
	public Object getItem(int arg0) {
		return arg0;
	}

	@Override
	public long getItemId(int position) {
		return position;
	}


	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		View listItem = convertView;

		LayoutInflater inflater = ((Activity) mContext).getLayoutInflater();
		listItem = inflater.inflate(R.layout.sublistadapter, parent, false);
		ImageView imageViewIcon=(ImageView) listItem.findViewById(R.id.imageViewIcon);
		TextView textViewName=(TextView) listItem.findViewById(R.id.textViewName);
		TextView textViewDesc=(TextView) listItem.findViewById(R.id.textViewDesc);
		if(position==0)
			imageViewIcon.setBackgroundResource(R.drawable.wedding_venue);
		else if(position==1)
			imageViewIcon.setBackgroundResource(R.drawable.bridal_fashion);
		else  if(position==2)
			imageViewIcon.setBackgroundResource(R.drawable.photogrphers);
		else  if(position==3)
			imageViewIcon.setBackgroundResource(R.drawable.makeup);
		else if(position==4)
			imageViewIcon.setBackgroundResource(R.drawable.caters);
		else  if(position==5)
			imageViewIcon.setBackgroundResource(R.drawable.floweres);
		else if(position==6)
			imageViewIcon.setBackgroundResource(R.drawable.dsicjokey);
		else if(position==7)
			imageViewIcon.setBackgroundResource(R.drawable.invitation);
		textViewName.setText(listItems.get(position));
		textViewDesc.setText("The standard chunk of lorem ipsum");

		return listItem;
	}
}
