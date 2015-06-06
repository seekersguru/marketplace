package com.calendar.activity;

import java.util.ArrayList;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.text.Html;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;

import com.calendar.adapter.SlidingIMagesAdapter;
import com.calendar.model.ObjectDrawerItem;
import com.calendar.util.HorizontalListView;
import com.calendarapp.R;

public class SlidingImagesActivity extends FragmentActivity {

	Button btnBack, btnContactUs;
	Context mContext;
	//	ViewPager mPager;
	//	CirclePageIndicator mIndicator;
	//	int currentimageindex = 0;
	//	kim_ViewPagerAdapter topBannerAdapter;
	HorizontalListView lvSlidingImages;
	TextView img_name;
	ArrayList<ObjectDrawerItem> listItems;
	SlidingIMagesAdapter adapterSlidingImages;
	TextView tvTitle;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.slidingimages);
		mContext = SlidingImagesActivity.this;
		idInitialization();
	}

	private void idInitialization()
	{
		btnBack=(Button) findViewById(R.id.btnBack);
		btnContactUs=(Button) findViewById(R.id.btnContactUs);
		lvSlidingImages=(HorizontalListView) findViewById(R.id.lvSlidingImages);
		//		mPager = (ViewPager) findViewById(R.id.pager);
		tvTitle=(TextView) findViewById(R.id.tvTitle);
		btnContactUs.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				startActivity(new Intent(SlidingImagesActivity.this,ChatActivity.class));				
			}
		});
		//		mIndicator = (CirclePageIndicator) findViewById(R.id.indicator);
		img_name=(TextView) findViewById(R.id.img_name);
		listItems=new ArrayList<ObjectDrawerItem>();
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
		adapterSlidingImages=new SlidingIMagesAdapter(mContext, listItems);
		lvSlidingImages.setAdapter(adapterSlidingImages);

		//		topBannerAdapter = new kim_ViewPagerAdapter(SlidingImagesActivity.this,listItems);
		//		mPager.setAdapter(topBannerAdapter);
		//		mIndicator.setViewPager(mPager);
		//		mPager.setCurrentItem(currentimageindex);
		btnBack.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				((SlidingImagesActivity)mContext).finish();				
			}
		});
		tvTitle.setText(Html.fromHtml("<b>Title:</b> Lorem Ipsum"));
		img_name.setText(Html.fromHtml("<b>Description:</b> The lorem ipsum text is typically a scrambled section of De finibus bonorum et malorum, " +
				"a 1st-century BC Latin text by Cicero, with words altered, added, and removed to make it nonsensical, improper" +
				" Latin." +
				"A variation of the ordinary lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was " +
				"popularized by advertisements for Letraset transfer sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which employed it in graphics and word processing templates for its desktop publishing program, PageMaker, for the Apple Macintosh."));
		//		mPager.setOnClickListener(new OnClickListener() {
		//
		//			@Override
		//			public void onClick(View v) {
		//				startActivity(new Intent(SlidingImagesActivity.this,ChatActivity.class));	
		//			}
		//		});
		//		mPager.setOnPageChangeListener(new OnPageChangeListener() {
		//
		//			@Override
		//			public void onPageSelected(int pageNumber) {
		//				mIndicator.setCurrentItem(pageNumber);
		//			}

		//			@Override
		//			public void onPageScrolled(int arg0, float arg1, int arg2) {
		//
		//			}
		//
		//			@Override
		//			public void onPageScrollStateChanged(int arg0) {
		//
		//			}
		//		});
	}
}
