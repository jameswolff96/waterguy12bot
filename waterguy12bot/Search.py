import traceback
from datetime import datetime
import DatabaseHandler
import Config

def isValidSubmission(submission, reddit):
    try:
        if (DatabaseHandler.submissionExists(submission.id)):
            return False

        try:
            if (submission.author.name == Config.USERNAME):
                DatabaseHandler.addSubmission(submission.id, submission.author.name, submission.subreddit, False)
                return False
        except:
            pass

        return True

    except:
        traceback.print_exc()
        return False
