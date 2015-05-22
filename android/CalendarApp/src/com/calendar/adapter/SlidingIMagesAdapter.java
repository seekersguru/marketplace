package com.calendar.adapter;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import com.calendar.model.ObjectDrawerItem;
import com.calendarapp.R;

public class SlidingIMagesAdapter  extends BaseAdapter{

	Context mContext;
	ArrayList<ObjectDrawerItem> listSlidingImages;

	public SlidingIMagesAdapter(Context mContext,ArrayList<ObjectDrawerItem> listSlidingImages)
	{
		this.mContext=mContext;
		this.listSlidingImages=listSlidingImages;	
	}
	@Override
	public int getCount() {
		return listSlidingImages.size();
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
		View listItem=convertView;
		LayoutInflater inflater = ((Activity) mContext).getLayoutInflater();
		listItem = inflater.inflate(R.layout.slidingimageshorizontallist, parent, false);
		ImageView imageViewIcon=(ImageView) listItem.findViewById(R.id.imageViewIcon);
		imageViewIcon.setImageResource(listSlidingImages.get(position).icon);
		return listItem;
	}

}
