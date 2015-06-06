package com.calendar.fragments;

import java.util.ArrayList;

import com.calendar.activity.SubListCategoryActivity;
import com.calendar.adapter.HomeMenuAdapter;
import com.calendar.model.ObjectDrawerItem;
import com.calendarapp.HomeActivity;
import com.calendarapp.R;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

public class HomeFragment extends BaseFragment {

	ListView lvImages;
	HomeMenuAdapter adapterHomeMenu;
	ArrayList<ObjectDrawerItem> listItems;

	@Override
	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		View view=inflater.inflate(R.layout.homefragment, container, false);
		idInitialization(view);
		return view;
	}

	private void idInitialization(View view){
		lvImages=(ListView) view.findViewById(R.id.lvImages);
		listItems=new ArrayList<ObjectDrawerItem>();	
		ObjectDrawerItem item1=new ObjectDrawerItem(R.drawable.wedding_venue, "Wedding Venues");
		listItems.add(item1);
		ObjectDrawerItem item2=new ObjectDrawerItem(R.drawable.bridal_fashion, "Bridal Fashion");
		listItems.add(item2);
		ObjectDrawerItem item3=new ObjectDrawerItem(R.drawable.photogrphers, "Photographers");
		listItems.add(item3);
		ObjectDrawerItem item4=new ObjectDrawerItem(R.drawable.makeup, "Makeup");
		listItems.add(item4);
		ObjectDrawerItem item5=new ObjectDrawerItem(R.drawable.caters, "Caterers");
		listItems.add(item5);
		ObjectDrawerItem item6=new ObjectDrawerItem(R.drawable.floweres, "Flowers");
		listItems.add(item6);
		ObjectDrawerItem item7=new ObjectDrawerItem(R.drawable.dsicjokey, "Disc jockeys");
		listItems.add(item7);
		ObjectDrawerItem item8=new ObjectDrawerItem(R.drawable.invitation, "Invitations");
		listItems.add(item8);
		adapterHomeMenu=new HomeMenuAdapter(mContext, listItems);
		lvImages.setAdapter(adapterHomeMenu);
		lvImages.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> arg0, View viewChild, int position,
					long arg3) {
				try {
					((HomeActivity)mContext).startActivity(new Intent(getActivity().getApplicationContext(),SubListCategoryActivity.class));
				} catch (Exception e) {
					e.getMessage();
				}
			}
		});
	}
}
