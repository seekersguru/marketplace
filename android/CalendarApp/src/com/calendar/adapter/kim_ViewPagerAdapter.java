package com.calendar.adapter;

import java.util.ArrayList;

import android.annotation.SuppressLint;
import android.content.Context;
import android.graphics.Bitmap;
import android.os.Parcelable;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.calendar.model.ObjectDrawerItem;
import com.calendar.util.ScaleImageView;

public class kim_ViewPagerAdapter extends PagerAdapter {
	public static String cond,wind,humidity,temp,date,min_temp,max_temp,min_max,country;
	public static Bitmap mBitmap;
	public static LinearLayout mLayout;
	public ScaleImageView image;
	//	ImageLoader imageLoader; 
	ArrayList<ObjectDrawerItem> slideimageList = new ArrayList<ObjectDrawerItem>();
	Context mContext;

	public kim_ViewPagerAdapter(Context mContext, ArrayList<ObjectDrawerItem> slideimageList) {
		this.mContext = mContext;
		this.slideimageList = slideimageList;
	}

	public int getCount(){
		return slideimageList.size();
	}
		private int dpToPx(int dp)
		{
			float density = mContext.getResources().getDisplayMetrics().density;
			return Math.round((float)dp * density);
		}
	@SuppressLint("NewApi")
	public Object instantiateItem(View collection, final int position) {

		image = new ScaleImageView(mContext);
		mLayout=new LinearLayout(mContext);
		@SuppressWarnings("deprecation")
		LayoutParams mLayoutParams=new LayoutParams(LayoutParams.FILL_PARENT,dpToPx(260));
		image.setLayoutParams(mLayoutParams);
		image.setScaleType(ImageView.ScaleType.FIT_XY);
		mLayout.setLayoutParams(mLayoutParams);
		image.setPadding(0, 0, 0, 0);
		image.setLeft(0);
		image.setRight(0);
		image.setTop(0);
		image.setBottom(0);
		image.setImageResource(slideimageList.get(position).icon);
		/*if(activityName.equals("DogaActivity"))
		{
			HashMap<String, String> news = new HashMap<String, String>();
			news = slideimageList.get(position);
			imageLoader.DisplayImage(news.get("SlideImageView"),  image);
		}
		else if(activityName.equals("tabTurler") || activityName.equals("tabFoto") || activityName.equals("tabVideo") || activityName.equals("tabMake") || activityName.equals("tabDirectory"))
		{
			image.setScaleType(ImageView.ScaleType.FIT_XY);
			if(!slidingImageList.get(position).equals(""))
			{
				strImagePath=slidingImageList.get(position).substring(slidingImageList.get(position).indexOf("h"), slidingImageList.get(position).indexOf(".jpg")+4);
				strImagePathValue=strImagePath.replace("\\","");
			}
			imageLoader.DisplayImage(strImagePathValue, image);
		}*/
		/*Drawable drawing = image.getDrawable();
		if (drawing == null) {
			return new Object(); // Checking for null & return, as suggested in comments
		}
		Bitmap bitmap = ((BitmapDrawable)drawing).getBitmap();

		// Get current dimensions AND the desired bounding box
		int width = bitmap.getWidth();
		int height = bitmap.getHeight();
		int bounding = dpToPx(250);
		Log.i("Test", "original width = " + Integer.toString(width));
		Log.i("Test", "original height = " + Integer.toString(height));
		Log.i("Test", "bounding = " + Integer.toString(bounding));

		// Determine how much to scale: the dimension requiring less scaling is
		// closer to the its side. This way the image always stays inside your
		// bounding box AND either x/y axis touches it.  
		float xScale = ((float) bounding) / width;
		float yScale = ((float) bounding) / height;
		float scale = (xScale <= yScale) ? xScale : yScale;
		Log.i("Test", "xScale = " + Float.toString(xScale));
		Log.i("Test", "yScale = " + Float.toString(yScale));
		Log.i("Test", "scale = " + Float.toString(scale));

		// Create a matrix for the scaling and add the scaling data
		Matrix matrix = new Matrix();
		matrix.postScale(scale, scale);
		//(activity.getWindowManager().getDefaultDisplay().getWidth()<scaledBitmap.getWidth()?scaledBitmap.getWidth():(activity.getWindowManager().getDefaultDisplay().getWidth())); // re-use
		// Create a new bitmap and convert it to a format understood by the ImageView 
		Bitmap scaledBitmap = Bitmap.createBitmap(bitmap, 0, 0, width, height, matrix, true);
		width = scaledBitmap.getWidth(); // re-use
		height = scaledBitmap.getHeight(); // re-use
		BitmapDrawable result = new BitmapDrawable(scaledBitmap);
		Log.i("Test", "scaled width = " + Integer.toString(width));
		Log.i("Test", "scaled height = " + Integer.toString(height));

		// Apply the scaled bitmap
		image.setImageDrawable(result);

		// Now change ImageView's dimensions to match the scaled image
		//		ViewGroup.LayoutParams params = (ViewGroup.LayoutParams) image.getLayoutParams(); 
		//		params.width = width;
		//		params.height = height;
		//		image.setLayoutParams(params);
		//		mLayout.setLayoutParams(params);

		Log.i("Test", "done");*/
		mLayout.addView(image);
		((ViewPager) collection).addView(mLayout);
		//		mLayout.setOnClickListener(new OnClickListener() {
		//			
		//			@Override
		//			public void onClick(View v) {
		//				// TODO Auto-generated method stub
		//				Log.i("setOnClickListener", "collection");
		//				 Intent intent1 = new Intent(activity, ImageActivity.class);
		//				 int ii=TrackActivity.getCurrentItem();
		//				 Log.i("ibOnClickTrackTrash", ""+TrackActivity.listTrackFile.get(ii));
		////				 intent1.putExtra("Image", TrackActivity.listTrackFile.get(ii));
		////				 activity.startActivity(intent1);
		//				 Intent i = new Intent(activity, FullScreenViewActivity.class);
		//					i.putExtra("position", ii);
		//					 activity.startActivity(i);
		//			}
		//		});

		return mLayout;
	}

	@Override
	public void destroyItem(View arg0, int arg1, Object arg2)
	{
		((ViewPager) arg0).removeView((View) arg2);
	}

	@Override
	public boolean isViewFromObject(View arg0, Object arg1) {
		return arg0 == ((View) arg1);
	}

	@Override
	public Parcelable saveState() {
		return null;
	}
}
