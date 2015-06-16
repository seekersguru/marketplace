package com.wedwise.adapter;

import java.util.ArrayList;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.wedwiseapp.FavData;
import com.wedwiseapp.R;

public class FavAdapter extends BaseAdapter {

	private Context mContext;
	private LayoutInflater infalter;
	private ArrayList<FavData> data = new ArrayList<FavData>();

	public FavAdapter(Context c) {
		infalter = (LayoutInflater) c
				.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
		mContext = c;
	}

	@Override
	public int getCount() {
		// return data.size();
		return 20;
	}

	@Override
	public FavData getItem(int position) {
		return data.get(position);
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	public void addAll(ArrayList<FavData> files) {

		try {

			this.data.clear();
			this.data.addAll(files);

		} catch (Exception e) {

		}

		notifyDataSetChanged();
	}

	public void add(FavData files) {

		try {
			this.data.add(files);
		} catch (Exception e) {

		}

		notifyDataSetChanged();
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {

		ViewHolder holder;
		if (convertView == null) {
			holder = new ViewHolder();

			convertView = infalter.inflate(R.layout.favorite_item, null);
			// holder.tvMenuTitle = (TextView) convertView;

			convertView.setTag(holder);

		} else {
			holder = (ViewHolder) convertView.getTag();
		}

		try {
			// holder.tvMenuTitle.setText(data.get(position).title);
		} catch (Exception e) {

		}

		return convertView;
	}

	public class ViewHolder {
		TextView tvMenuTitle;
	}

}
