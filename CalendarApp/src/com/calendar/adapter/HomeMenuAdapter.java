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
import com.calendar.model.ObjectDrawerItem;
import com.calendarapp.R;

public class HomeMenuAdapter extends BaseAdapter{

	Context mContext;
	ArrayList<ObjectDrawerItem> listItems;
	public HomeMenuAdapter(Context mContext,ArrayList<ObjectDrawerItem> listItems)
	{
		this.mContext=mContext;
		this.listItems=listItems;
	}

	@Override
	public int getCount() {
		// TODO Auto-generated method stub
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
		listItem = inflater.inflate(R.layout.homemenuadapter, parent, false);
		ImageView imageViewIcon=(ImageView) listItem.findViewById(R.id.imageViewIcon);
		TextView textViewName=(TextView) listItem.findViewById(R.id.textViewName);
		imageViewIcon.setImageResource(listItems.get(position).icon);
        textViewName.setText(listItems.get(position).name);
        
		return listItem;
	}

}
