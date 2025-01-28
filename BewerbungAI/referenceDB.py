import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BewerbungAI.settings')
django.setup()

from WebApplication.models import Data, UserProfile


def link_user_to_data():
    for user in UserProfile.objects.all():
        try:
            # Filtering data 
            dataEntries = Data.objects.filter(email=user.email)

            for data_entry in dataEntries:
                data_entry.user_profile = user
                data_entry.save()
                print(f"Linked {user.username} to {data_entry}")

            if dataEntries.exists():
                print(f"\nUser {user.username} data history:")
                for data in dataEntries:
                    print(f"- {data.firstname} {data.lastname} ({data.jobFieldName})")

        except Exception as e:
            print(f"Error linking data to {user.username}: {e}")


if __name__ == "__main__":
    link_user_to_data()